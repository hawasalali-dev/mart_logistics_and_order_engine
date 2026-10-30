class InvalidItemError(Exception):
    pass


class Item:
    def __init__(self, name, price):
        if price <= 0:
            raise InvalidItemError("Preis muss größer als 0 sein.")

        self.name = name
        self.price = price


class PhysicalItem(Item):
    def __init__(self, name, price, weight_kg):
        super().__init__(name, price)
        self.weight_kg = weight_kg


class DigitalItem(Item):
    def __init__(self, name, price, download_link):
        super().__init__(name, price)
        self.download_link = download_link
        self.weight_kg = 0.0


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self, discount_fn=None):
        total = sum(item.price for item in self.items)

        if discount_fn:
            total = discount_fn(total)

        return total