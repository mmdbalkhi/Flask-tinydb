import io
import os
import sys
from typing import Any, Dict, Optional

from tinydb import Storage as _Storage
from tinydb.storages import JSONStorage, MemoryStorage, touch

__all__ = (
    "JSONStorage",
    "MemoryStorage",
    "YAMLStorage",
)


class Storage(_Storage):  # pragma: no cover (it is a copy from tinydb.JSONStorage)
    def __init__(
        self, path: str, create_dirs=False, encoding=None, access_mode="r+", **kwargs
    ) -> None:
        """
        Create a new instance.

        Also creates the storage file, if it doesn't exist and the access mode is appropriate for writing.

        :param path: Where to store the JSON data.
        :param access_mode: mode in which the file is opened(r, r+, w, a, x, b, t, +, U)
        :type access_mode: str
        """

        super().__init__()

        self._mode = access_mode
        self.kwargs = kwargs

        # Create the file if it doesn't exist and creating is allowed by the
        # access mode
        if any(
            [character in self._mode for character in ("+", "w", "a")]
        ):  # any of the writing modes
            touch(path, create_dirs=create_dirs)

        # Open the file for reading/writing
        self._handle = open(path, mode=self._mode, encoding=encoding)

    def close(self) -> None:
        self._handle.close()


try:
    import yaml
except ImportError:  # pragma: no cover
    import warnings

    warnings.warn(
        "pyyaml lib is Not Installed. If you want to use yaml,"
        "you must be install pyyaml via this command: \n"
        "pip install Flask-TinyDB[yaml]"
    )
    sys.exit(1)


class YAMLStorage(Storage):
    """Store the data in a Yaml file.

    usage:
        ...
        >>> app.config["TINYDB_DATABASE_STORAGE"] = YAMLStorage
        >>> db = TinyDB(app)
        ...
    """

    def read(self) -> Optional[Dict[str, Dict[str, Any]]]:
        # Get the file size by moving the cursor to the file end and reading
        # its location
        self._handle.seek(0, os.SEEK_END)
        size = self._handle.tell()

        if not size:
            # File is empty, so we return ``None`` so TinyDB can properly
            # initialize the database
            return None

        self._handle.seek(0)
        return yaml.safe_load(self._handle.read())

    def write(self, data: Dict[str, Dict[str, Any]]) -> None:
        # Move the cursor to the beginning of the file just in case
        self._handle.seek(0)

        # Serialize the database state using the user-provided arguments
        serialized = yaml.dump(data, **self.kwargs)

        # Write the serialized data to the file
        try:
            self._handle.write(serialized)
        except io.UnsupportedOperation as err:  # pragma: no cover
            raise OSError(
                f'Cannot write to the database. Access mode is "{self._mode}"'
            ) from err

        # Ensure the file has been written
        self._handle.flush()
        os.fsync(self._handle.fileno())

        # Remove data that is behind the new cursor in case the file has
        # gotten shorter
        self._handle.truncate()
