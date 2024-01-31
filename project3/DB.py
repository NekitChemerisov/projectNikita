import sqlite3
class DB():

    def __init__(self):
        self.connection = sqlite3.connect('project3/taskmanager.db')
        self.cursor = self.connection.cursor()

    def create_table_users(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        phone INTEGER,
        password TEXT NOT NULL
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        body TEXT NOT NULL,
        date DATETIME
        )
        ''')

    def close(self):
        self.connection.close()