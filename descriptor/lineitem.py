"""
==============
LineItem tests
==============

A line item for a bulk food order has description, weight and price fields::

    >>> raisins = LineItem('Golden raisins', 10, 6.95)
    >>> raisins.quantity, raisins.product, raisins.price
    (10, 'Golden raisins', 6.95)

A ``total`` method gives the total price for that line item::

    >>> raisins.total()
    69.5

"""
class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity
        