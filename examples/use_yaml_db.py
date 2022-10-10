from flask import Flask

from flask_tinydb import TinyDB
from flask_tinydb.storages import YAMLStorage

app = Flask(__name__)
app.config["TINYDB_DATABASE_STORAGE"] = YAMLStorage
db = TinyDB(app)


@app.route("/")
def index():
    all_pets = db.get_table().all()
    return ", ".join([value["name"] for value in all_pets]) if all_pets else "No pets"


@app.route("/add/<pet>")
def add(pet):
    db.get_table().insert({"name": pet})
    return f"Added {pet}"


if __name__ == "__main__":
    app.run()
