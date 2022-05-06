from pathlib import Path

from tinydb import Query
from tinydb import TinyDB

from flask_tinydb import YAMLStorage


def test_yaml_storage():

    # Create a temporary YAML file
    path = Path(__file__).parent / "test_storage.yaml"

    # remove it if it exists
    if path.exists():
        path.unlink()

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
