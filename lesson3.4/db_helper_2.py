import sqlite3
from sqlite3 import Error

class DBHelper:
    def __init__(self,db_path = "my_database.db"):
        self.db_path = db_path
        self.initialize_db()

    def connect(self):
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            conn.execute("PRAGMA foreign_keys = ON")
            return conn
        except Error as e:
            print(f"Ошибка подключения к БД: {e}")
            raise


    def initialize_db(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT NOT UNIQUE
        );
        """
        conn = sqlite3.connect()
        try:
            conn.execute(sql)
            conn.commit()
        finally:
            conn.close()

    def add_user(self, name, age, email = None):
        sql = "INSERT INTO users (name, age, email) VALUES (?, ?, ?)"
        conn = self.connect()
        try:
            cur = conn.cursor()
            cur.execute(sql, (name, age, email))
            conn.commit()
            return cur.lastrowid
        except Error as e:
            print(f"Ошибка при добавлении пользователя: {e}")
            raise
        finally:
            conn.close()

    def get_all_users(self):
        sql = "SELECT * FROM users"
        conn = self.connect()
        try:
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            return cur.fetchall()
        finally:
            conn.close()

    def find_user(self, keyword):
        sql = "SELECT * FROM users WHERE name LIKE ? OR email LIKE ?"
        like = f"%{keyword}%"
        conn = self.connect()
        try:
            cur = conn.cursor()
            cur.execute(like, like)
            return cur.fetchall()
        finally:
            conn.close()
            