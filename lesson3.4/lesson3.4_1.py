"""
СУБД - Система Управления Базы Данных
работа с sql
гарантирует целостность
контроль транзакции
доступ параллельный между многими пользователями
производительность
виды sql:
my sql
sqlite
mongodb
cassanda
postgress
"""

# import sqlite3
#
# conn = sqlite3.connect('database.db')
#
# cursor = conn.cursor()
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER
# )
# """)
#
# conn.commit()  #фиксирует изменения
#
# conn.close()




import  sqlite3
def init_db(db_path = "my_database.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        )
    """)

    conn.commit()
    conn.close()

def add_user(name, age, db_path="my_database.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

def get_all_users(db_path="my_database.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT id, name, age FROM users")  #[(1: "Alice" 30 years old)]
    rows = cur.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()

    add_user("Алиса", 30)
    add_user("Боб", 25)

    users = get_all_users()
    for vid, name, age in users:
        print(f"{vid}: {name} {age} лет")
