#from todo import *
class TodoList:
    def __init__(self):
        self.task_list = []


    def add(self, todo):
        self.task_list.append(todo)
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
    
    def incomplete(self):
        incomplete_list = []
        for task in self.task_list:
            if task.complete == False:
                incomplete_list.append(task)
        return incomplete_list
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        complete_list = []
        for task in self.task_list:
            if task.complete == True:
                complete_list.append(task)
        return complete_list

    def give_up(self):
        given_up_list = []
        for task in self.task_list:
            task.mark_complete()
            given_up_list.append(task)
        return given_up_list

        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        


