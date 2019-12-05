# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_location, items=None):
        self.current_location = current_location
        self.name = name
        if (items is None):
            self.loot = []


        else:
            self.loot = items

    def __str__(self):
        return f"{self.name}"

    def get_loot(self, item):
        self.loot.append(item)
        print(f"You have added {item.name} to your stash of loot")



