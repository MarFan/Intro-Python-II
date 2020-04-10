class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_item(self, item):
        print(f"\t{item.name}: {item.description}\n")
