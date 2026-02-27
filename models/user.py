import sqlite3
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash


class User:

    @staticmethod
    def create(username, password):
        conn = sqlite3.connect(Config.DATABASE_PATH)
        c = conn.cursor()

        hashed_password = generate_password_hash(password)

        try:
            c.execute("""
                INSERT INTO users (username, password)
                VALUES (?, ?)
            """, (username, hashed_password))

            conn.commit()
            conn.close()
            return True
        except:
            conn.close()
            return False

    @staticmethod
    def authenticate(username, password):
        conn = sqlite3.connect(Config.DATABASE_PATH)
        c = conn.cursor()

        c.execute("SELECT id, password FROM users WHERE username = ?", (username,))
        user = c.fetchone()

        conn.close()

        if user and check_password_hash(user[1], password):
            return user[0]  # return user_id

        return None