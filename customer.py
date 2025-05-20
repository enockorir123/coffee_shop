
from order import Order
from coffee import Coffee

class Customer:
    """
    Represents a customer in the coffee shop.
    """

    def __init__(self, name: str):
        # validated via setter
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        """
        Return a list of Order instances for this customer.
        """
        return [order for order in Order._all_orders if order.customer is self]

    def coffees(self):
        """
        Return a unique list of Coffee instances this customer has ordered.
        """
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee: Coffee, price: float):
        """
        Create a new Order linking this customer to a coffee at given price.
        """
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee: Coffee):
        """
        Return the Customer who has spent the most on the given coffee.
        If no orders for that coffee, return None.
        """
        spend = {}
        for order in Order._all_orders:
            if order.coffee is coffee:
                spend.setdefault(order.customer, 0.0)
                spend[order.customer] += order.price
        if not spend:
            return None
        return max(spend, key=spend.get)
