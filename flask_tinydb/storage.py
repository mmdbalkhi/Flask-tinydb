"""
Storage module for Flake-tinyDB.
=================================

This module contains the Storage class.

usage:
-------

.. code-block:: python

    from flask_tinydb import Storage, TinyDB
    from flask import Flask

    app = Flask(__name__)
    db = TinyDB(app, storage=YAMLStorage)

    ...
"""
from pathlib import Path
from typing import Any
from typing import Dict
from typing import Optional

import yaml
from tinydb import Storage


class YAMLStorage(Storage):
    """YAML Storage is a tinydb storage that uses YAML to store data."""

    def __init__(self, filename: str = "db.yaml") -> None:
        """Initialize YAMLStorage.

        :args:
            - `filename`: path to the YAML file
        """
        self.filename = Path(filename)

        if not self.filename.exists():
            self.filename.touch()

    def read(self) -> Optional[Dict[str, Dict[str, Any]]]:
        """Read data from YAML file.

        :returns:
            - `data`: data from YAML file
            - `None`: if file does not exist
        """
        with open(self.filename) as handle:
            data = yaml.safe_load(handle.read())  # (2)
            return data

    def write(self, data: Dict[str, Dict[str, Any]]) -> None:
        """Write data to YAML file.

        :args:
            - `data`: data to be written to YAML file
        """
        with open(self.filename, "w+") as handle:
            yaml.dump(data, handle)
