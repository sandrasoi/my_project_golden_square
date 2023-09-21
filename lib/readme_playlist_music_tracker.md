# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class Playlist():
    def __init__(self, name):
        #Parameter:
        #   name: string
        #Side effects:
        #   Sets the name property of the self object

    def add_track(self, track_name):
        #Paramater:
        # track_name: string representing name of a track to be added
        #Returns
        #   Nothing
        #Side effect
        #   Track gets added to a list

    def view_tracks(self):
        #Paramater:
        #   None
        #Returns:
        #   List of all the tracks


## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""Given a name and a song,
list the song given.
"""

playlist = Playlist("Best songs")
playlist.add_track("Song 1")
playlist.view_tracks() #=> "Song 1"

"""Given a name and several songs,
list all songs given.
"""

playlist = Playlist("Best songs")
playlist.add_track("Song 1")
playlist.add_track("Song 2")
playlist.add_track("Song 3")
playlist.view_tracks() #=> "Song 1, Song 2, Song 3"

"""Given a name and no song,
return error with the message "No tracks given"
"""
playlist = Playlist("Best songs")
playlist.view_tracks() #=> raises an error with message "No tracks given"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->