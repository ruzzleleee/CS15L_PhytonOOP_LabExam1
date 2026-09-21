class Inventory:
    def __init__(self):
        self.items = []

    # methods
    def search(self, name):
        """Case-insensitive search. Returns the item or None."""
        for item in self.items:
            if item.name.lower() == name.strip().lower():
                return item
        return None

    def add_item(self, item):
        """Add an item. Rejects duplicate item names."""
        if self.search(item.name) is not None:
            raise ValueError(f"'{item.name}' already exists in the inventory.")
        self.items.append(item)

    def update_quantity(self, name, qty):
        """Add stock to an existing item by name."""
        item = self.search(name)
        if item is None:
            raise ValueError(f"Item '{name}' was not found.")
        item.restock(qty)

    def display_all(self):
        if len(self.items) == 0:
            print("The inventory is empty.")
            return
        for number, item in enumerate(self.items, start=1):
            print(f"\n--- Item {number} ---")
            item.display()

    def total_inventory_value(self):
        total = 0
        for item in self.items:
            total += item.total_value()
        return total