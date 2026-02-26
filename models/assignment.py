import sqlite3
from config import Config

class Assignment:

    @staticmethod
    def create(subject_id, title, deadline):
        conn = sqlite3.connect(Config.DATABASE_PATH)
        c = conn.cursor()

        c.execute("""
            INSERT INTO assignments (subject_id, title, deadline)
            VALUES (?, ?, ?)
        """, (subject_id, title, deadline))

        conn.commit()
        conn.close()

    @staticmethod
    def get_by_subject(subject_id):
        conn = sqlite3.connect(Config.DATABASE_PATH)
        c = conn.cursor()

        c.execute("""
            SELECT id, title, deadline, status, created_at
            FROM assignments
            WHERE subject_id = ?
            ORDER BY created_at DESC
        """, (subject_id,))

        assignments = c.fetchall()
        conn.close()
        return assignments