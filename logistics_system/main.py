from logistics.models import PhysicalItem, DigitalItem, Order
from logistics.discounts import (
    vip_discount,
    black_friday_discount
)
from logistics.shipping import ShippingCalculator


keyboard = PhysicalItem("Tastatur", 79.99, 1.2)
monitor = PhysicalItem("Monitor", 249.99, 5.5)
software = DigitalItem(
    "Software Lizenz",
    59.99,
    "https://download.com/license"
)

order = Order()

order.add_item(keyboard)
order.add_item(monitor)
order.add_item(software)

expensive_products = list(
    filter(lambda item: item.price > 50, order.items)
)

print("Produkte über 50€:")

for item in expensive_products:
    print(f"{item.name} - {item.price}€")

normal = order.calculate_total()
black_friday = order.calculate_total(black_friday_discount)
vip = order.calculate_total(vip_discount)

print("\nNormaler Preis:", normal)
print("Black Friday Preis:", round(black_friday, 2))
print("VIP Preis:", round(vip, 2))

shipping_costs = ShippingCalculator.calculate_shipping(order)

print("Versandkosten:", shipping_costs)