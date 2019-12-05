# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        if (items is None):
            self.room_loot = []


        else:
            self.room_loot = items
    def __str__(self):
        return f"{self.name}"

    def remove_loot(self, name):


        taken_item = next((item for item in self.room_loot if item.name == name), None)

        if taken_item is not None:
            self.room_loot.remove(taken_item)
            return taken_item
        else:
            return None


