from pathlib import Path

from tinydb import Query
from tinydb import TinyDB

from flask_tinydb import YAMLStorage


def test_yaml_storage():
    # Create a temporary YAML file
    path = Path(__file__).parent / "test_storage.yaml"

    try:
        path.unlink()
    except FileNotFoundError:
        path.touch()

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


def test_yaml_storage_if_file_not_exists():

    # Create a temporary YAML file
    path = Path(__file__).parent / "test_storage.yaml"

    try:
        path.unlink()
    except FileNotFoundError:  # pragma: no cover
        pass
    storage = YAMLStorage

    # Create a TinyDB instance
    db = TinyDB(path, storage=storage)

    name = Query()

    db.insert({"name": "John Doe"})
    assert db.all() == [{"name": "John Doe"}]
