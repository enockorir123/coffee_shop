
from customer import Customer
from coffee import Coffee

class Order:
    #epresents a single coffee order by a customer.
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
        if isinstance(value, float) and 100.0 <= value <= 1000.0:
            self._price = value
        else:
            raise ValueError("Price must be  between  KSH 100.0 and 1000.0.")
        
if __name__ == "__main__":
    # Create some coffee products
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")

    # Create a customer
    customer1 = Customer("Alice")

    # Create orders
    order1 = customer1.create_order(coffee1, 300.50)
    order2 = customer1.create_order(coffee2, 110.00)

    # Print order details
    print(f"{customer1.name} ordered {coffee1.name} for KSH {order1.price}")
    print(f"{customer1.name} ordered {coffee2.name} for KSH {order2.price}")

    # Show coffee statistics
    print(f"{coffee1.name} has been ordered {coffee1.num_orders()} times.")
    print(f"The average price for {coffee1.name} is KSH {coffee1.average_price():.2f}.")
