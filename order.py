

from customer import Customer
from coffee import Coffee

class Order:
    """
    Represents a single coffee order by a customer.
    """
    _all_orders = []

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        # TODO: validate inputs and set attributes
        #       then append self to Order._all_orders
        pass

    @property
    def customer(self) -> Customer:
        # TODO: return the Customer instance
        pass

    @property
    def coffee(self) -> Coffee:
        # TODO: return the Coffee instance
        pass

    @property
    def price(self) -> float:
        # TODO: return the price
        pass

    @price.setter
    def price(self, value: float):
        # TODO: validate and set price
        pass
