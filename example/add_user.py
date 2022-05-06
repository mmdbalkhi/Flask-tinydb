from flask import Flask
from flask import jsonify

from flask_tinydb import TinyDB

app = Flask(__name__)
db = TinyDB(app).get_db()


@app.route("/<username>")
def index(username):
    db.insert({"name": username})
    return f"{username} added to database"


@app.route("/users")
def users():
    return jsonify(db.all())


if __name__ == "__main__":
    app.run()
