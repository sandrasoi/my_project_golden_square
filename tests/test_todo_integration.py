from lib.todo import *
from lib.todo_list import *


def test_adding_two_todos_and_viewing_them():
    todolist = TodoList()
    todo_one = Todo('Task 1')
    todo_two = Todo('Task 2')
    todolist.add(todo_one)
    todolist.add(todo_two)
    result = todolist.incomplete()
    assert result == [todo_one,todo_two]

def test_view_completed_tasks():
    todolist = TodoList()
    todo_one = Todo('Task 1')
    todo_two = Todo('Task 2')
    todolist.add(todo_one)
    todolist.add(todo_two)
    todo_one.mark_complete()
    result = todolist.complete()
    assert result == [todo_one]

def test_all_todos_completed():
    todolist = TodoList()
    todo_one = Todo('Task 1')
    todo_two = Todo('Task 2')
    todolist.add(todo_one)
    todolist.add(todo_two)
    result = todolist.give_up()
    assert result == [todo_one, todo_two]