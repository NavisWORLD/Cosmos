from cosmos.core.provenance import QuantumRecord, derive_seed, verify_record


def test_provenance_seed_is_deterministic_and_labeled():
    record = QuantumRecord("ibm", "backend-x", ("0101", "1110"), "hardware", "job-1")
    assert verify_record(record)["binary"]
    assert derive_seed(record, [60.0, 0.5]) == derive_seed(record, [60.0, 0.5])
    changed = QuantumRecord("ibm", "backend-x", ("0101", "1111"), "hardware", "job-1")
    assert derive_seed(record) != derive_seed(changed)
