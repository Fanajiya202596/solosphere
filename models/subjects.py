import sqlite3
from config import Config


class Subject:

    @staticmethod
    def create(name):
        conn = sqlite3.connect(Config.DATABASE_PATH)
        c = conn.cursor()

        c.execute(
            "INSERT INTO subjects (name) VALUES (?)",
            (name,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect(Config.DATABASE_PATH)
        c = conn.cursor()

        c.execute("SELECT id, name, created_at FROM subjects ORDER BY created_at DESC")

        subjects = c.fetchall()

        conn.close()

        return subjects