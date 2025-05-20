

class Coffee:
    """
    Represents a coffee product in the shop.
    """

    def __init__(self, name: str):
        # TODO: validate and set self._name
        pass

    @property
    def name(self) -> str:
        # TODO: return coffee name
        pass

    @name.setter
    def name(self, value: str):
        # TODO: validate and set name
        pass

    def orders(self):
        """Return a list of Order instances for this coffee."""
        # TODO: filter Order._all_orders
        pass

    def customers(self):
        """Return a unique list of Customer instances who ordered this coffee."""
        # TODO: derive from orders()
        pass

    def num_orders(self) -> int:
        """Total times this coffee has been ordered."""
        # TODO: return len(self.orders())
        pass

    def average_price(self) -> float:
        """Average price paid for this coffee."""
        # TODO: compute from orders()
        pass
