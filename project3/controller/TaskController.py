import sys
sys.path.append('C:/Users/cheme/OneDrive/Документы/python/projectNikita/project3')
import DB

class Task():

    def __init__(self):
        self.db = DB.DB()

    def setup_database(self):
        self.db.create_table_users() 
        self.db.close()

app = Task()
app.setup_database()