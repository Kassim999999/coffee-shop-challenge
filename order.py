from customer import Customer
from coffee import Coffee
class Order:

    _all = []

    def __init__(self,customer, coffee, price):

        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("praise must be be a float between 1.0 and 10.0")
        
        self.customer = customer
        self.coffe = coffee
        self.price = price
        Order._all.append(self)

    @property
    def price(self):
        return self._price
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee