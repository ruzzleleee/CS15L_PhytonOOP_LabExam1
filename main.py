"""main.py - Menu-driven Inventory System."""

from items import Item, PerishableItem, ElectronicItem
from inventory import Inventory

# input helpers
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_text(prompt):
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("Input cannot be empty.")



def add_item(inventory):
    print("\nItem type: ",
    "\n1) Regular" ,
    "\n2) Perishable ",
    "\n3) Electronic")
    choice = input("Choose type: ").strip()
    if choice not in ("1", "2", "3"):
        print("Invalid item type.")
        return

    name = get_text("Item name: ")
    quantity = get_int("Quantity: ")
    price = get_float("Price: ")

    try:
        if choice == "1":
            item = Item(name, quantity, price)
        elif choice == "2":
            days = get_int("Days until expiry: ")
            item = PerishableItem(name, quantity, price, days)
        else:
            warranty = get_int("Warranty (months): ")
            item = ElectronicItem(name, quantity, price, warranty)

        inventory.add_item(item)
        print(f"'{item.name}' added successfully.")
    except ValueError as error:
        print(f"Error: {error}")


def restock_item(inventory):
    name = get_text("Item name to restock: ")
    qty = get_int("Quantity to add: ")
    try:
        inventory.update_quantity(name, qty)
        print("Stock updated.")
    except ValueError as error:
        print(f"Error: {error}")


def sell_item(inventory):
    name = get_text("Item name to sell: ")
    item = inventory.search(name)
    if item is None:
        print(f"Item '{name}' was not found.")
        return

    qty = get_int("Quantity to sell: ")
    try:
        item.sell(qty)
        print(f"Sold {qty} of '{item.name}'. Remaining: {item.get_quantity()}")
    except ValueError as error:
        print(f"Error: {error}")


def search_item(inventory):
    name = get_text("Item name to search: ")
    item = inventory.search(name)
    if item is None:
        print(f"Item '{name}' was not found.")
    else:
        print()
        item.display()


def show_menu():
    print("\n===== INVENTORY SYSTEM =====")
    print("1. Add item")
    print("2. Restock")
    print("3. Sell")
    print("4. Search")
    print("5. Display all items")
    print("6. Show total inventory value")
    print("7. Exit")


def main():
    inventory = Inventory()

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            restock_item(inventory)
        elif choice == "3":
            sell_item(inventory)
        elif choice == "4":
            search_item(inventory)
        elif choice == "5":
            inventory.display_all()
        elif choice == "6":
            print(f"Total inventory value: {inventory.total_inventory_value():.2f}")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()