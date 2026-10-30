from logistics.models import PhysicalItem


class ShippingCalculator:

    @staticmethod
    def calculate_shipping(order):

        total_weight = sum(
            item.weight_kg
            for item in order.items
            if isinstance(item, PhysicalItem)
        )

        if total_weight < 2:
            return 4.99
        elif total_weight <= 10:
            return 9.99
        else:
            return 19.99