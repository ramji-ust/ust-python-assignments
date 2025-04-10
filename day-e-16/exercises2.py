import sqlite3

conn = sqlite3.connect('school.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    grade TEXT
)
''')

students_to_insert = [
    ('Alice', 14, '8th'),
    ('Bob', 15, '9th'),
    ('Charlie', 13, '7th')
]

cursor.executemany('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', students_to_insert)

print("Inserted students:\n")

cursor.execute('SELECT * FROM students')
all_students = cursor.fetchall()

for student in all_students:
    print(student)