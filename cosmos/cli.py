from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform
import sys

from . import __version__
from .config import CosmosConfig
from .core.provenance import QuantumRecord, derive_seed, verify_record
from .core.state import Dyn12State, GaussianStateKernel, preflight
from .integration import probe_http
from .runtime import CosmosRuntime
from .tools.evidence import EvidenceLedger
from .web import serve


def _json(value: object) -> None:
    print(json.dumps(value, indent=2, ensure_ascii=False, default=str))


def cmd_info(_: argparse.Namespace) -> int:
    _json({"name": "COSMOS", "version": __version__, "python": platform.python_version(), "platform": platform.platform()})
    return 0


def cmd_doctor(args: argparse.Namespace) -> int:
    cfg = CosmosConfig.from_env()
    cfg.ensure_dirs()
    checks = [
        {"name": "python", "ok": sys.version_info >= (3, 10), "detail": platform.python_version()},
        {"name": "data_dir", "ok": cfg.data_dir.exists(), "detail": str(cfg.data_dir.resolve())},
    ]
    ollama = probe_http("ollama", f"{cfg.ollama_url.rstrip('/')}/api/tags", timeout=args.timeout)
    checks.append({"name": ollama.name, "ok": ollama.ok, "detail": ollama.detail, "optional": True})
    _json({"ok": all(c["ok"] for c in checks if not c.get("optional")), "checks": checks})
    return 0 if all(c["ok"] for c in checks if not c.get("optional")) else 1


def cmd_demo(_: argparse.Namespace) -> int:
    cfg = CosmosConfig.from_env()
    cfg.backend = "echo"
    with CosmosRuntime(cfg) as runtime:
        first = runtime.process_turn("COSMOS demo: remember that the compact state has twelve scalars.")
        second = runtime.process_turn("What did the demo say about the compact state?")
        _json({"first": first.response, "second": second.response, "recalled": second.memories, "status": runtime.status()})
    return 0


def cmd_chat(_: argparse.Namespace) -> int:
    cfg = CosmosConfig.from_env()
    print(f"COSMOS {__version__} | backend={cfg.backend} | /exit to quit")
    with CosmosRuntime(cfg) as runtime:
        while True:
            try:
                message = input("you> ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                return 0
            if message in {"/exit", "/quit"}:
                return 0
            if not message:
                continue
            try:
                result = runtime.process_turn(message)
                print(f"cosmos> {result.response}")
            except Exception as exc:
                print(f"error> {exc}")


def cmd_web(args: argparse.Namespace) -> int:
    cfg = CosmosConfig.from_env()
    if args.host:
        cfg.host = args.host
    if args.port:
        cfg.port = args.port
    serve(cfg)
    return 0


def cmd_evidence_verify(args: argparse.Namespace) -> int:
    ledger = EvidenceLedger(Path(args.path))
    ok, count, error = ledger.verify()
    _json({"ok": ok, "events": count, "error": error, "path": str(ledger.path)})
    return 0 if ok else 1


def cmd_state_preflight(_: argparse.Namespace) -> int:
    state = Dyn12State()
    states = [state.update([0.05 * (i + j) for j in range(12)]) for i in range(4)]
    kernel = GaussianStateKernel()
    matrix = kernel.matrix(states)
    _json({"bandwidth": kernel.bandwidth, "preflight": preflight(states, matrix)})
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cosmos", description="COSMOS local-first research runtime")
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("info", help="show version and environment")
    p.set_defaults(func=cmd_info)

    p = sub.add_parser("doctor", help="run non-destructive health checks")
    p.add_argument("--timeout", type=float, default=1.0)
    p.set_defaults(func=cmd_doctor)

    p = sub.add_parser("demo", help="run a dependency-free local loop demo")
    p.set_defaults(func=cmd_demo)

    p = sub.add_parser("chat", help="interactive local chat using configured backend")
    p.set_defaults(func=cmd_chat)

    p = sub.add_parser("web", help="serve local JSON API")
    p.add_argument("--host")
    p.add_argument("--port", type=int)
    p.set_defaults(func=cmd_web)

    p = sub.add_parser("evidence-verify", help="verify a hash-chained evidence ledger")
    p.add_argument("path", nargs="?", default="var/evidence.jsonl")
    p.set_defaults(func=cmd_evidence_verify)

    p = sub.add_parser("state-preflight", help="exercise dyn12 state/kernel liveness checks")
    p.set_defaults(func=cmd_state_preflight)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.func(args))
