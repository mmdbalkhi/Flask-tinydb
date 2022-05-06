import tinydb
from flask import Flask


class TinyDB:
    """tinydb class for flask"""

    def __init__(self, app: Flask = None) -> None:
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        app.config.setdefault("TINYDB_DATABASE_PATH", "flask.db")
        app.config.setdefault("TINYDB_DATABASE_TABLE", "app")
        app.config.setdefault("TINYDB_DATABASE_STORAGE", tinydb.storages.JSONStorage)
        print(app.config["TINYDB_DATABASE_STORAGE"])
        self.db = tinydb.TinyDB(
            app.config["TINYDB_DATABASE_PATH"],
            storage=app.config["TINYDB_DATABASE_STORAGE"],
        )
        self.table = self.db.table(
            app.config["TINYDB_DATABASE_TABLE"],
        )

    def get_db(self) -> tinydb.TinyDB:
        """Get the underlying TinyDB instance."""
        return self.db

    def get_table(self) -> tinydb.table.Table:
        """Get the underlying TinyDB Table instance."""
        return self.table
