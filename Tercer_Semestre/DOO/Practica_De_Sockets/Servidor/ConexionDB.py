import sqlite3


class ColegioDB:

    _DATABASE = "ColegioDB.db"
    _conexion = None
    _cursor = None

    def __enter__(self):
        self._conexion = sqlite3.connect(self._DATABASE)
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cursor.close()
        self._conexion.commit()
        self._conexion.close()
