from task_manager import Task
class Storage():
    def __init__(self, file_path):
        self.file_path = file_path

    def add_task(self, task):
        with open(self.file_path, 'a') as file:
            file.write(f"{task.task_name},{task.date},{task.description},{task.status}\n")

    def delete_task(self, task_name):
        tasks = self.get_all_tasks()
        tasks = [task for task in tasks if task.task_name != task_name]
        with open(self.file_path, 'w') as file:
            for task in tasks:
                file.write(f"{task.task_name},{task.date},{task.description},{task.status}\n")

    def get_all_tasks(self):
        tasks = []
        with open(self.file_path, 'r') as file:
            for line in file:
                task_name, date, description, status = line.strip().split(',')
                tasks.append(Task(task_name, date, description, status))
        return tasks
    
    