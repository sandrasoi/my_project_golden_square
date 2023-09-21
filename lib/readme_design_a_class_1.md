# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class Tasks():
    def __init__(self):
        pass

    def add_todo_task(self, task):
        #Parameters:
        #   task: string representing a single task
        #Returns:
        #   Nothing
        #Side effects:
        #   Saves the task to the self object

    def view_tasks(self):
        #Returns:
        #   List all tasks that have been added

    def mark_task_complete(self, completed_task):
        #Paramaters:
        #   completed_task: Seleted task to be marked as completed
        #Returns:
        #   string statating a task has been deleted and list of tasks updated
        #Side effects:
        #   Deletes completed_task from list of tasks

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a task, returns list of tasks
"""
task = Tasks()
task.add_todo_task("Walk the dog")
task.view_tasks() # => "Walk the dog"

"""
Given two tasks, marking one as complete, 
return all remaining tasks
"""
task = Tasks()
task.add_todo_task("Walk the dog")
task.add_todo_task("Wash dishes")
task.mark_task_complete("Walk the dog")
task.view_tasks() #=> "Wash dishes"

"""
Given no task set, return an error with message:
'No task set.'
"""
task = Tasks()
task.view_tasks() # = > raises an error with message "No task set."


#_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->