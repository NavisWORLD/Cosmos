from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import blake2b
import json
from math import sqrt
from pathlib import Path
import re
import sqlite3
from typing import Iterable, Sequence

TOKEN_RE = re.compile(r"[A-Za-z0-9_']+")


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def _cosine(a: Sequence[float], b: Sequence[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b, strict=True))
    na = sqrt(sum(x * x for x in a))
    nb = sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


class HashingEmbedder:
    """Small deterministic local retrieval baseline with no model download.

    It is intentionally a lexical hashing baseline, not a claim of deep semantic understanding.
    A production deployment can replace it with a purpose-built embedding adapter.
    """

    def __init__(self, dimensions: int = 256) -> None:
        if dimensions < 16:
            raise ValueError("dimensions must be at least 16")
        self.dimensions = dimensions

    def encode(self, text: str) -> list[float]:
        vector = [0.0] * self.dimensions
        tokens = [t.lower() for t in TOKEN_RE.findall(text)]
        for token in tokens:
            digest = blake2b(token.encode("utf-8"), digest_size=16).digest()
            index = int.from_bytes(digest[:8], "big") % self.dimensions
            sign = 1.0 if digest[8] & 1 else -1.0
            vector[index] += sign
        norm = sqrt(sum(v * v for v in vector))
        return [v / norm for v in vector] if norm else vector


@dataclass(frozen=True, slots=True)
class Memory:
    id: int
    text: str
    tags: tuple[str, ...]
    importance: float
    created_at: str
    score: float = 0.0


class SQLiteMemoryStore:
    """Durable local memory with pluggable vectorization and Hebbian associations."""

    def __init__(self, path: str | Path, embedder: HashingEmbedder | None = None) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.embedder = embedder or HashingEmbedder()
        self._db = sqlite3.connect(self.path)
        self._db.execute("PRAGMA journal_mode=WAL")
        self._db.execute(
            """CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                tags TEXT NOT NULL,
                importance REAL NOT NULL,
                created_at TEXT NOT NULL,
                vector TEXT NOT NULL
            )"""
        )
        self._db.execute(
            """CREATE TABLE IF NOT EXISTS associations (
                left_term TEXT NOT NULL,
                right_term TEXT NOT NULL,
                weight REAL NOT NULL,
                updates INTEGER NOT NULL,
                PRIMARY KEY(left_term, right_term)
            )"""
        )
        self._db.commit()

    def close(self) -> None:
        self._db.close()

    def __enter__(self) -> "SQLiteMemoryStore":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def remember(self, text: str, tags: Iterable[str] = (), importance: float = 0.5) -> int:
        text = text.strip()
        if not text:
            raise ValueError("memory text cannot be empty")
        importance = min(1.0, max(0.0, float(importance)))
        cleaned_tags = tuple(sorted({tag.strip().lower() for tag in tags if tag.strip()}))
        vector = self.embedder.encode(text)
        cursor = self._db.execute(
            "INSERT INTO memories(text, tags, importance, created_at, vector) VALUES (?, ?, ?, ?, ?)",
            (text, json.dumps(cleaned_tags), importance, _utcnow(), json.dumps(vector)),
        )
        self._update_associations(text)
        self._db.commit()
        return int(cursor.lastrowid)

    def recall(self, query: str, limit: int = 5) -> list[Memory]:
        if limit <= 0:
            return []
        qvec = self.embedder.encode(query)
        rows = self._db.execute(
            "SELECT id, text, tags, importance, created_at, vector FROM memories"
        ).fetchall()
        ranked: list[Memory] = []
        now = datetime.now(timezone.utc)
        for row in rows:
            created = datetime.fromisoformat(row[4])
            age_days = max(0.0, (now - created).total_seconds() / 86400.0)
            recency = 1.0 / (1.0 + age_days / 30.0)
            similarity = _cosine(qvec, json.loads(row[5]))
            score = 0.78 * similarity + 0.14 * float(row[3]) + 0.08 * recency
            ranked.append(
                Memory(
                    id=int(row[0]),
                    text=row[1],
                    tags=tuple(json.loads(row[2])),
                    importance=float(row[3]),
                    created_at=row[4],
                    score=score,
                )
            )
        ranked.sort(key=lambda item: (item.score, item.id), reverse=True)
        return ranked[:limit]

    def count(self) -> int:
        row = self._db.execute("SELECT COUNT(*) FROM memories").fetchone()
        return int(row[0])

    def top_associations(self, term: str, limit: int = 10) -> list[tuple[str, float, int]]:
        term = term.lower().strip()
        rows = self._db.execute(
            """SELECT left_term, right_term, weight, updates
               FROM associations
               WHERE left_term = ? OR right_term = ?
               ORDER BY weight DESC, updates DESC LIMIT ?""",
            (term, term, limit),
        ).fetchall()
        out: list[tuple[str, float, int]] = []
        for left, right, weight, updates in rows:
            out.append((right if left == term else left, float(weight), int(updates)))
        return out

    def _update_associations(self, text: str) -> None:
        terms = sorted(set(t.lower() for t in TOKEN_RE.findall(text) if len(t) > 2))[:32]
        for i, left in enumerate(terms):
            for right in terms[i + 1 :]:
                self._db.execute(
                    """INSERT INTO associations(left_term, right_term, weight, updates)
                       VALUES (?, ?, 1.0, 1)
                       ON CONFLICT(left_term, right_term)
                       DO UPDATE SET weight = associations.weight * 0.995 + 1.0,
                                     updates = associations.updates + 1""",
                    (left, right),
                )
