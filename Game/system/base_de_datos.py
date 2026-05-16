import sqlite3
import os

from Game.main import BASE_DIR

DB_PATH = os.path.join(BASE_DIR, "db.sqlite3")


def iniciar_base_de_datos() -> None:
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    con.executescript("""
            CREATE TABLE  ;

        """)


