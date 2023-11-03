import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("SELECT country FROM countries WHERE area >= ?", (2000000, ))
rows = cursor.fetchall()
connection.close()

print(rows)