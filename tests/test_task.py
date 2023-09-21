from lib.task import *

def test_view_tasks():
    task = Tasks()
    task.add_todo_task("Walk the dog")
    result = task.view_tasks()
    assert result == "Walk the dog"

def test_marking_task_as_complete():
    task = Tasks()
    task.add_todo_task("Walk the dog")
    task.add_todo_task("Wash dishes")
    task.mark_task_complete("Walk the dog")
    result = task.view_tasks() 
    assert result == "Wash dishes"

def test_no_task_set():
    task = Tasks()
    result = task.view_tasks() 
    assert result == "No task set."