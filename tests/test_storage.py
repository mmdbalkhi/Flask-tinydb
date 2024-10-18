import tempfile

from tinydb import Query, TinyDB

from flask_tinydb.storages import YAMLStorage


def test_yaml_storage():
    path = tempfile.mkstemp()[1]

    storage = YAMLStorage

    # Create a TinyDB instance
    db = TinyDB(path, storage=storage)

    name = Query()

    db.insert({"name": "John Doe"})
    assert db.all() == [{"name": "John Doe"}]

    db.insert({"name": "Another John Doe"})
    assert db.all() == [{"name": "John Doe"}, {"name": "Another John Doe"}]

    db.update({"name": "John Doe II"}, name.name == "John Doe")
    assert db.all() == [{"name": "John Doe II"}, {"name": "Another John Doe"}]

    db.remove(name.name == "John Doe II")
    assert db.all() == [{"name": "Another John Doe"}]
