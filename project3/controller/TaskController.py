import sys
sys.path.append('C:/Users/cheme/OneDrive/Документы/python/projectNikita/project3')
from DB import DB

class TaskController:
    def __init__(self):
        self.db = DB()
        self.db.create_tables()

    def add_task(self, title, body, date, username):
        self.db.add_task(title, body, date, username)

    def delete_task(self, task_id):
        self.db.delete_task(task_id)

    def clear_tasks(self, username):
        self.db.clear_tasks(username)

    def get_tasks(self, username):
        return self.db.get_tasks(username)

    def close_database(self):
        self.db.close()
        

# app = DB()
# app.create_tables()