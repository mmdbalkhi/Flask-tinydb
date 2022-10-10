import unittest

from flask import Flask

from flask_tinydb import TinyDB

app = Flask(__name__)
client = app.test_client()


class TestTinyDB(unittest.TestCase):
    def test_init(self):
        db = TinyDB(app)
        assert db.get_table() is not None

    def test_insert(self):
        db = TinyDB(app).get_db()
        assert db.insert({"test": "test"})

    def test_read(self):
        db = TinyDB(app).get_db()
        assert db.all()[0] == {"test": "test"}
