class Tasks():
    def __init__(self):
        self.total_tasks = []

    def add_todo_task(self, task):
        self.total_tasks.append(task)

    def view_tasks(self):
        if self.total_tasks == []:
            return "No task set."
        else:
            return ' '.join(self.total_tasks)
    
    def mark_task_complete(self, completed_task):
        self.total_tasks.remove(completed_task)

