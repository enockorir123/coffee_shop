
from customer import Customer
from coffee import Coffee

class Order:
    """
    Represents a single coffee order by a customer.
    """
    _all_orders = []

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        # use setters for validation
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order._all_orders.append(self)

    @property
    def customer(self) -> Customer:
        return self._customer

    @customer.setter
    def customer(self, value: Customer):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise TypeError("customer must be an instance of Customer class.")

    @property
    def coffee(self) -> Coffee:
        return self._coffee

    @coffee.setter
    def coffee(self, value: Coffee):
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise TypeError("coffee must be an instance of Coffee class.")

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")
