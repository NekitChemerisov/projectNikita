import sqlite3

class DB:
    def __init__(self):
        self.connection = sqlite3.connect('project3/taskmanager.db')
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            phone TEXT,
            password TEXT NOT NULL
        )''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            body TEXT,
            date TEXT,
            name TEXT,
            FOREIGN KEY(name) REFERENCES Users(name)
        )''')
        self.connection.commit()

    def add_task(self, title, body, date, name):
        self.cursor.execute('''
        INSERT INTO Tasks (title, body, date, name) VALUES (?, ?, ?, ?)
        ''', (title, body, date, name))
        self.connection.commit()

    def delete_task(self, task_id):
        self.cursor.execute('''
        DELETE FROM Tasks WHERE id = ?
        ''', (task_id,))
        self.connection.commit()

    def clear_tasks(self, name):
        self.cursor.execute('''
        DELETE FROM Tasks WHERE name = ?
        ''', (name,))
        self.connection.commit()

    def get_tasks(self, name):
        self.cursor.execute('''
        SELECT id, title, body, date FROM Tasks WHERE name = ?
        ''', (name,))
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
