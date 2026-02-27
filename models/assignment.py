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
    
    @staticmethod
    def update_status(assignment_id, status):
        conn = sqlite3.connect(Config.DATABASE_PATH)
        c = conn.cursor()

        # Check if assignment exists
        c.execute("SELECT id FROM assignments WHERE id = ?", (assignment_id,))
        assignment = c.fetchone()

        if not assignment:
            conn.close()
            return False  # Not found

        c.execute("""
            UPDATE assignments
            SET status = ?
            WHERE id = ?
        """, (status, assignment_id))

        conn.commit()
        conn.close()
        return True
    @staticmethod
    def delete(assignment_id):
        conn = sqlite3.connect(Config.DATABASE_PATH)
        c = conn.cursor()

        c.execute("""
            DELETE FROM assignments
            WHERE id = ?
        """, (assignment_id,))

        conn.commit()
        conn.close()
    @staticmethod
    def get_stats():
        conn = sqlite3.connect(Config.DATABASE_PATH)
        c = conn.cursor()

        # Total assignments
        c.execute("SELECT COUNT(*) FROM assignments")
        total = c.fetchone()[0]

        # Completed
        c.execute("SELECT COUNT(*) FROM assignments WHERE status = 'completed'")
        completed = c.fetchone()[0]

        # Pending
        c.execute("SELECT COUNT(*) FROM assignments WHERE status = 'pending'")
        pending = c.fetchone()[0]

        conn.close()

        return {
            "total": total,
            "completed": completed,
            "pending": pending
        }
