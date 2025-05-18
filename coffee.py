class Coffee:
    _all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 3:
            raise ValueError("Name must be atleast 3 characters long.")
        self._name = name

    @property
    def name(self):
        return self._name
    
    def orders(self):
        return[order for order in Order._all if order.coffee == self]
    
    def customers(self):
        return list(set(order.customer for order in self.orders()))
    
    def number_of_orders(self):
        return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if prices else 0 