Storage
==========

Unfortunately Tinydb only support :class:`~tinydb.storages.JSONStorage` and
:class:`~tinydb.storages.MemoryStorage` storage. because this, I add some popular
file types like :class:`.storages.YAMLStorage`.

.. code-block:: python

    ...
    app.config["TINYDB_DATABASE_STORAGE"] = YAMLStorage
    db = TinyDB(app)
    ...

of cource you can use your custom text-file storage method with :class:`.storages.Storage` class:

.. code-block:: python

    from flask_tinydb.storages import Storage

    class MyStorageMethod(Storage):
        def read(self):
            # do_something

        def write(self):
            # do_something

    app.config["TINYDB_DATABASE_STORAGE"] = MyStorageMethod
    db = TinyDB(app)
    ...
