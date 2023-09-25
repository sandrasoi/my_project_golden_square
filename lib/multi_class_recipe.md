# Journal Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_


  ┌───────────────────────────────────────────────┐
  │  class Diary()                                │
  │                                               │
  │  diary_entries()                              │
  │                                               │
  │  todo_list()                                  │
  │                                               │
  │  phone_number_list()                          │
  │                                               │
  │  find_best_entry_for_reading_time(wpm,minutes)│
  │                                               │
  │                                               │
  └─────────────────┬─────────────────────────────┘
                    │
                    │
                    ▼
  ┌─────────────────────────────────────┐
  │  class DiaryEntry(title, contents)  │
  │                                     │
  │    self.title = tile                │
  │    self.contents = contents         │
  │                                     │
  │   is_todo()                         │
  │                                     │
  │   is_phone_number()                 │
  │                                     │
  │   count_words()                     │
  │                                     │
  │   reading_time(wpm)                 │
  └─────────────────────────────────────┘


_Also design the interface of each class in more detail._

class Diary():

    def __init__(self):
        self.entry_list

    def add(title, contents):
        Params:
            title: str
            contents: str
        Effect:
            add entry to a list

    def diary_entries(self):
        Params:
            None
        Returns:
            A list of all diary entries

    def todo_list():
        Params:
            None
        Returns:
            A list of all todo entries

    def phone_number_list():
        Params:
            None
        Returns:
            A list of all phone numbers

    def find_best_entry_for_reading_time(wpm, minutes):
        # Parameters:
            #   wpm:     an integer representing the number of words the user can
            #            read per minute
            #   minutes: an integer representing the number of minutes the user has
            #            to read
        # Returns:
            #   A list of all diary entries that meet the criteria (within the given time and reading speed)

class DiaryEntry(title, contents):

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def is_todo():
        Param:
            None
        Effects:
            Return boolean if todo is in the contents

    def is_phone_number():
        Param:
            None
        Effect:
            Return boolean if phone number is in the contents
    
    def count_words():
        Param:
            None
        Return:
            Length of content

    def reading_time(wpm):
        Param: 
            wpm: words per minute (int)
        Returns:
            Time taken to read content

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

"""
Given multiple entries added
Return list of entries
"""
diary = Diary()
diary_entry1 = DiaryEntry("Title1", "Contents1")
diary_entry2 = DiaryEntry("Title2", "Contents2")
diary.add(diary_entry1)
diary.add(diary_entry2)
diary.diary_entries() => [diary_entry1, diary_entry2]

def test_best_entry_to_read_given_wpm1_time_2():
    diary = Diary()
    diary_entry1 = DiaryEntry("title1", "One Two")
    diary_entry2 = DiaryEntry("title2", "Three Four Five")
    diary_entry3 = DiaryEntry("title2", "Six Seven Eight Nine")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    result = diary.find_best_entry_for_reading_time(1,2)
    assert result == "One Two"

def test_best_entry_to_read_given_wpm1_time_2():
    diary = Diary()
    diary_entry0 = DiaryEntry("title0", 'One')
    diary_entry1 = DiaryEntry("title1", "One Two")
    diary_entry2 = DiaryEntry("title2", "Three Four Five")
    diary_entry3 = DiaryEntry("title2", "Six Seven Eight Nine")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    result = diary.find_best_entry_for_reading_time(1,2)
    assert result == [diary_entry0, diary_entry1]

def test_phone_number_list():
    diary = Diary()
    diary_entry0 = DiaryEntry("title0", 'words words words 07802000000')
    diary_entry1 = DiaryEntry("title1", "One Two")
    diary_entry2 = DiaryEntry("title2", "07802123456")
    diary_entry3 = DiaryEntry("title2", "Six Seven Eight Nine")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    result = diary.phone_number_list()
    assert result == [07802000000, 07802123456]

def test_list_of_todos(): 
    diary = Diary()
    diary_entry0 = DiaryEntry("title0", '07802000000')
    diary_entry1 = DiaryEntry("title1", "Todo One Two")
    diary_entry2 = DiaryEntry("title2", "07802123456")
    diary_entry3 = DiaryEntry("title2", "Todo Six Seven Eight Nine")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    result = diary.todo_list()
    assert result == ["Todo One Two", "Todo Six Seven Eight Nine"]

#Diary doesn't have parameters, has add method that calls instance of diary entry




## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->