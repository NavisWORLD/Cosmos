from cosmos.core.memory import SQLiteMemoryStore


def test_memory_persists_and_recalls(tmp_path):
    path = tmp_path / "memory.sqlite3"
    with SQLiteMemoryStore(path) as store:
        store.remember("the dyn12 mechanism uses twelve compact scalars", tags=("cst",), importance=0.9)
        store.remember("bananas are yellow", tags=("noise",), importance=0.1)
        assert store.count() == 2
    with SQLiteMemoryStore(path) as store:
        results = store.recall("dyn12 twelve scalars", limit=2)
        assert results[0].text.startswith("the dyn12")
        assert store.count() == 2
