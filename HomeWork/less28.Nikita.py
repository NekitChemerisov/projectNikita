import sqlite3

'''try:
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO person (name, lastname) VALUES (?, ?)', ('Иван', 'Иванов'))
    cursor.execute('UPDATE person SET lastname = ? WHERE name = ?', ('Сидоров', 'Иван'))

    connection.commit()

except Exception as e:
    connection.rollback()
    print(f"Произошла ошибка: {e}")

finally:
    connection.close()'''

try:
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()

    cursor.execute('SAVEPOINT sp1')

    cursor.execute('INSERT INTO person (name, lastname) VALUES (?, ?)', ('Иван', 'Иванов'))
    cursor.execute('UPDATE person SET lastname = ? WHERE name = ?', ('Сидоров', 'Иван'))

    connection.commit()

except Exception as e:
    cursor.execute('ROLLBACK TO SAVEPOINT sp1')

    connection.commit()
    print(f"Произошла ошибка: {e}")

finally:
    connection.close()