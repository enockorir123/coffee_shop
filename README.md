Coffee Shop Domain Model

A simple Python application that uses object-oriented programming to model a coffee shop.  
It includes three classes: Customer, Coffee, and Order, and shows how they relate.

 FEATURES
Customer  
•	Create a customer with a validated name.  
•	View all orders and coffees purchased.  
•	Create new orders.  
•	Find the top spender for a given coffee.

Coffee 
•	Create a coffee with a validated name.  
•	View all orders and customers for that coffee.  
•	Get total order count and average price.

Order  
•	Links one customer, one coffee, and a price.  
•	Validates all inputs.  
•	Tracks every order in a central list.
PROJECT STRUCTURE
coffee_shop/
├── customer.py    # Defines the Customer class and its behaviors
├── coffee.py      # Defines the Coffee class and its behaviors
├── order.py       # Defines the Order class and tracks all orders
└── README.md      # This file, explaining setup and project layout
