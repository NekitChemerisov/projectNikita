import sqlite3

connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()


cursor.execute('INSERT INTO person (name, lastname, course) VALUES (?, ?, ?)', ('Петр', 'Петров', 'Python для продвинутых'))

connection.commit()
connection.close()