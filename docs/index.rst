.. flask-tinydb documentation master file, created by
   sphinx-quickstart on Fri May  6 23:20:47 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to flask-tinydb's documentation!
========================================

flask-tinydb is a Flask extension that provides a TinyDB database.


requirements
----------------

- Python 3.7+
- Flask 2.0+
- TinyDB 4.0+


install
-----------------

via pip::

    pip install flask-tinydb

via source::

    git clone https://github.com/mmdbalkhi/flask-tinydb.git
    cd flask-tinydb
    python setup.py install


usage
-----------------

.. code-block:: python

    from flask import Flask, jsonify
    from flask_tinydb import TinyDB

    app = Flask(__name__)
    db = TinyDB(app).get_db()

    @app.route('/<username>')
    def index(username):
        db.insert({'name': username})
        return f"{username} added to database"

    @app.route('/users')
    def users():
        return jsonify(db.all())

    if __name__ == '__main__':
        app.run()


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
   storage

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
