"""
Flask-tinydb
=================

flask-tinydb is a Flask extension that provides a TinyDB database.

.. codeauthor:: komeil Parseh <ahmdparsh129@gmail.com>

Usage example:

>>> from flask import Flask, jsonify
>>> from flask_tinydb import TinyDB
>>> app = Flask(__name__)
>>> db = TinyDB(app).get_db()

>>> @app.route('/<username>')
def index(username):
    db.insert({'name': username})
    return f"{username} added to database"
>>> @app.route('/users')
def users():
    return jsonify(db.all())
>>> app.run()
 * Serving Flask app '__main__' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
"""
from . import storages
from .tinydb import TinyDB

__version__ = "1.3.0"
