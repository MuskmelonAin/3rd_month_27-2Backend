import sqlite3

def init_db(db_path="new_database.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT,
            city TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def add_user(name, age, email, city, db_path="new_database.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age, email, city) VALUES (?, ?, ?, ?)",
                (name, age, email, city))
    conn.commit()
    conn.close()

def get_users_by_age_range(min_age, max_age, db_path="new_database.db"):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE age BETWEEN ? AND ?", (min_age, max_age))
    rows = cur.fetchall()
    conn.close()
    return rows

def get_recent_users(n, db_path="new_database.db"):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM users ORDER BY created_at DESC LIMIT ?", (n,))
    rows = cur.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()

    add_user("Елена", 28, "elena@example.com", "Москва")
    add_user("Игорь", 35, "igor@example.com", "Казань")
    add_user("Наташа", 22, "nata@example.com", "Москва")

    print("Пользователи от 25 до 35 лет:")
    for user in get_users_by_age_range(25, 35):
        print(dict(user))

    print("\nПоследние 2 пользователя:")
    for user in get_recent_users(2):
        print(dict(user))
