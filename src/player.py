# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __ini__(self, name, current_location):
        self.current_location = current_location
        self.name = name

