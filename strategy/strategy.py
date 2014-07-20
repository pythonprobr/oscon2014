# strategy.py
# Strategy pattern -- function-based implementation

#####################################################################
# Exercise 2
#
# Goal: make the STRATEGY_TESTS doctests pass
#
# Procedure:
#
# a) delete the Promotion class
# b) change the Promotion subclasses into functions but preserve
#    their docstrings
# c) run `python3 -m doctest strategy.py -f` to check your work 
#####################################################################

"""
# BEGIN STRATEGY_TESTS

    >>> joe = Customer('John Doe', 0)  # <1>
    >>> ann = Customer('Ann Smith', 1100)
    >>> cart = [LineItem('banana', 4, .5),
    ...         LineItem('apple', 10, 1.5),
    ...         LineItem('watermellon', 5, 5.0)]
    >>> Order(joe, cart, fidelity_promo)  # <2>
    <Order total: 42.00 due: 42.00>
    >>> Order(ann, cart, fidelity_promo)
    <Order total: 42.00 due: 39.90>
    >>> banana_cart = [LineItem('banana', 30, .5),
    ...                LineItem('apple', 10, 1.5)]
    >>> Order(joe, banana_cart, bulk_item_promo)  # <3>
    <Order total: 30.00 due: 28.50>
    >>> long_order = [LineItem(str(item_code), 1, 1.0)
    ...               for item_code in range(10)]
    >>> Order(joe, long_order, large_order_promo)  # <4>
    <Order total: 10.00 due: 9.30>
    >>> Order(joe, cart, large_order_promo)
    <Order total: 42.00 due: 42.00>

# END STRATEGY_TESTS
"""
# BEGIN STRATEGY

from abc import ABCMeta, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # the Context

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(metaclass=ABCMeta):  # the Strategy

    @abstractmethod
    def discount(self, order):
        """Return discount as an positive dollar amount"""


class FidelityPromo(Promotion):  # first Concrete Strategy
    """5% discount for customers with 1000 or more fidelity points"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # second Concrete Strategy
    """10% discount for each LineItem with 20 or more units"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):  # third Concrete Strategy
    """7% discount for orders with 10 or more distinct items"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0

# END CLASSIC_STRATEGY