class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description


class ShowItem:

    def __init__(self, item=None):
    	if item != None:
    		print(f"\t{item.name}: {item.description}")
