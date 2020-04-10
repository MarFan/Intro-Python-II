# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description, items=None, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description

        if items is None:
            self.items = []
        else:
            self.items = item

        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def dropped_item(self, item):
        """ A dropped item is added to the room """
        pass

    def picked_item(self, item):
        """ A picked item is removed from the room and added to player inventory """
        pass
