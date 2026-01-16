import requests
import sqlite3

url = "https://openlibrary.org/subjects/python.json?limit=5"
response = requests.get(url)
data = response.json()

books = data["works"]

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT
)
""")

for book in books:
    title = book["title"]
    author = book["authors"][0]["name"]
    cursor.execute(
        "INSERT INTO books (title, author) VALUES (?, ?)",
        (title, author)
    )

conn.commit()

cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

conn.close()
