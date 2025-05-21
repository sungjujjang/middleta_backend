import sqlite3
import os

def start_db():
    db_path = os.path.join(os.path.dirname(__file__), 'db.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    return conn, cursor

