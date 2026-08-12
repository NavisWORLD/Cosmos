import json

from cosmos.tools.evidence import EvidenceLedger


def test_hash_chain_detects_tampering(tmp_path):
    path = tmp_path / "ledger.jsonl"
    ledger = EvidenceLedger(path)
    ledger.append("BOOT", "OBSERVED", {"ok": True})
    ledger.append("BENCH", "NULL", {"metric": 0.0})
    assert ledger.verify() == (True, 2, None)
    lines = path.read_text().splitlines()
    record = json.loads(lines[0])
    record["payload"]["ok"] = False
    lines[0] = json.dumps(record)
    path.write_text("\n".join(lines) + "\n")
    ok, _, error = ledger.verify()
    assert not ok
    assert error
