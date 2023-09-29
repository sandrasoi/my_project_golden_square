# File: lib/secret_diary.py

class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.locked = True


    def read(self):
        if self.locked:
            raise Exception("Go away!")
        else:
            return self.diary.read()
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        

    def lock(self):
        self.locked = True
        # Locks the diary
        # Returns nothing
        

    def unlock(self):
        self.locked = False
        # Unlocks the diary
        # Returns nothing
        