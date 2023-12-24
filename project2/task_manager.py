class Task:
    def __init__(self, task_name, date, description, status):
        self.task_name = task_name
        self.date = date
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.task_name} - {self.date} - {self.description} - {self.status}"
