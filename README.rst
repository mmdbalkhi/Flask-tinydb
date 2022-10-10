Flask-tinydb
=================

flask-tinydb is a Flask extension that provides a TinyDB database.

- tiny 🔍
- fast 🚀
- simple 💡
- lightweight 📦
- typed ✨

requirements
----------------

- Python 3.8+
- Flask 1.0+
- TinyDB 4.0+
- pyyaml 6.0+(optinal)

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


Links
-----

-   Documentation: https://flask-tinydb.readthedocs.io/
-   Source Code: https://github.com/mmdbalkhi/flask-tinydb
-   Issue Tracker: https://github.com/mmdbalkhi/flask-tinydb/issues/
