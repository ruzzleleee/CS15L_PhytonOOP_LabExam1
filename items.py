class Item:

    def __init__(self, name, quantity, price):
        name = str(name).strip()
        if name == "":
            raise ValueError("Item name cannot be empty.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.name = name
        self.__quantity = quantity  
        self.__price = price         

    # getters
    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    # methods
    def restock(self, qty):
        if qty <= 0:
            raise ValueError("Restock quantity must be greater than zero.")
        self.__quantity += qty

    def sell(self, qty):
        if qty <= 0:
            raise ValueError("Sell quantity must be greater than zero.")
        if qty > self.__quantity:
            raise ValueError(
                f"Not enough stock. Only {self.__quantity} left of '{self.name}'."
            )
        self.__quantity -= qty

    def total_value(self):
        return self.get_quantity() * self.get_price()

    def display(self):
        print(f"Name       : {self.name}")
        print(f"Quantity   : {self.get_quantity()}")
        print(f"Price      : {self.get_price():.2f}")
        print(f"Total Value: {self.total_value():.2f}")


class PerishableItem(Item):
    DISCOUNT_RATE = 0.50      # 50% off
    EXPIRY_THRESHOLD = 3      # 3 days or fewer left
    LOW_STOCK_THRESHOLD = 5   # 5 or fewer stocks left

    def __init__(self, name, quantity, price, days_until_expiry):
        super().__init__(name, quantity, price)
        if days_until_expiry < 0:
            raise ValueError("Days until expiry cannot be negative.")
        self.days_until_expiry = days_until_expiry
    
    # methods
    def is_expiring_soon(self):
        return self.days_until_expiry <= self.EXPIRY_THRESHOLD
    
    def is_low_stock(self):
        return self.get_quantity() <= self.LOW_STOCK_THRESHOLD
    
    def has_discount(self):
        """Discount applies if expiring soon OR stock is low."""
        return self.is_expiring_soon() or self.is_low_stock()

    def get_price(self):
        # apply discount to price
        price = super().get_price()
        if self.has_discount():
            return price * (1 - self.DISCOUNT_RATE)
        return price

    def total_value(self):
        # apply dicount and calculate the total value
        return self.get_quantity() * self.get_price()

    def display(self):
        super().display()
        print(f"Expires In : {self.days_until_expiry} day(s)")
        if self.has_discount():
            original = super().get_price()
            reasons = []
            if self.is_expiring_soon():
                reasons.append("EXPIRING SOON")
            if self.is_low_stock():
                reasons.append("LOW STOCK")
            print(f"*** {' & '.join(reasons)} - 50% OFF (was {original:.2f}) ***")


class ElectronicItem(Item):

    def __init__(self, name, quantity, price, warranty_months):
        super().__init__(name, quantity, price)
        if warranty_months < 0:
            raise ValueError("Warranty months cannot be negative.")
        self.warranty_months = warranty_months

    def display(self):
        super().display()
        print(f"Warranty   : {self.warranty_months} month(s)")