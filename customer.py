

class Customer:
    """
    Represents a customer in the coffee shop.
    """

    def __init__(self, name: str):
        # TODO: validate and set self._name
        pass

    @property
    def name(self) -> str:
        # TODO: return customer name
        pass

    @name.setter
    def name(self, value: str):
        # TODO: validate and set name
        pass

    def orders(self):
        """Return a list of Order instances for this customer."""
        # TODO: filter Order._all_orders
        pass

    def coffees(self):
        """Return a unique list of Coffee instances this customer has ordered."""
        # TODO: derive from orders()
        pass

    def create_order(self, coffee, price: float):
        """Create a new Order linking this customer to a coffee at given price."""
        # TODO: instantiate Order(self, coffee, price)
        pass
