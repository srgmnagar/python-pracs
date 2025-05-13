import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

students_data = [
    ("Artur", 28, "A"),
    ("Mich", 29, "D"),
    ("Jhn", 23, "B"),
]

cursor.execute("""
    CREATE TABLE if not exists Students (
        name TEXT PRIMARY KEY,
        age INTEGER,
        grade TEXT
    )
""")

cursor.executemany("""
    INSERT INTO students
    (name, age, grade)
    VALUES (?, ?, ?)
""", students_data)
conn.commit()

cursor.execute("SELECT * FROM students")
all_students = cursor.fetchall()
print("Student Records:")
for student in all_students: print(student)

conn.close()