# db_setup.py
import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    department TEXT,
    salary REAL
)
''')

cursor.executemany('''
INSERT INTO employees (name, age, department, salary)
VALUES (?, ?, ?, ?)
''', [
    ("Alice", 30, "HR", 50000),
    ("Bob", 25, "Engineering", 70000),
    ("Charlie", 35, "Sales", 60000)
])

conn.commit()
conn.close()
