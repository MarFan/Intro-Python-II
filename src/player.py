# Write a class to hold player information, e.g. what room they are in
# currently.
class Character:

    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room

        if inventory is None:
        	self.inventory = []
        else:
        	self.inventory = inventory

    def add_item(self, item):
    	#print(f"{item.name} {item.description}")
    	self.inventory.append(item)

    def remove_item(self, item):
    	print(item.name)
