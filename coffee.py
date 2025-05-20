
from order import Order
from customer import Customer

class Coffee:
    """
    Represents a coffee product in the shop.
    """

    def __init__(self, name: str):
        # validated via setter
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")

    def orders(self):
        """
        Return a list of Order instances for this coffee.
        """
        return [order for order in Order._all_orders if order.coffee is self]

    def customers(self):
        """
        Return a unique list of Customer instances who have ordered this coffee.
        """
        return list({order.customer for order in self.orders()})

    def num_orders(self) -> int:
        """
        Total times this coffee has been ordered.
        """
        return len(self.orders())

    def average_price(self) -> float:
        """
        Average price paid for this coffee.
        """
        orders = self.orders()
        if not orders:
            return 0.0
        return sum(order.price for order in orders) / len(orders)
