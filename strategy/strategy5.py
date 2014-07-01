# classic_strategy.py
# Strategy pattern -- classic implementation

"""
# BEGIN CLASSIC_STRATEGY_TESTS

    >>> from promos import *
    >>> joe = Customer('John Doe', 0)  # <1>
    >>> ann = Customer('Ann Smith', 1100)
    >>> cart = [LineItem('banana', 4, .5),  # <2>
    ...         LineItem('apple', 10, 1.5),
    ...         LineItem('watermellon', 5, 5.0)]
    >>> Order(joe, cart, fidelity_promo)  # <3>
    <Order total: 42.00 due: 42.00>
    >>> Order(ann, cart, fidelity_promo)  # <4>
    <Order total: 42.00 due: 39.90>
    >>> banana_cart = [LineItem('banana', 30, .5),  # <5>
    ...                LineItem('apple', 10, 1.5)]
    >>> Order(joe, banana_cart, bulk_item_promo)  # <6>
    <Order total: 30.00 due: 28.50>
    >>> long_order = [LineItem(str(item_code), 1, 1.0) # <7>
    ...               for item_code in range(10)]
    >>> Order(joe, long_order, large_order_promo)  # <8>
    <Order total: 10.00 due: 9.30>
    >>> Order(joe, cart, large_order_promo)
    <Order total: 42.00 due: 42.00>

Best promo tests:

    >>> Order(joe, long_order, best_promo)
    <Order total: 10.00 due: 9.30>
    >>> Order(joe, banana_cart, best_promo)
    <Order total: 30.00 due: 28.50>
    >>> Order(ann, cart, best_promo)
    <Order total: 42.00 due: 39.90>



# END CLASSIC_STRATEGY_TESTS
"""
# BEGIN CLASSIC_STRATEGY
from collections import namedtuple
import inspect

import promos

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
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def best_promo(order):
    """Select best discount available
    """
    discounters = [func for name, func in
                    inspect.getmembers(promos, inspect.isfunction)]

    return max(promo(order) for promo in discounters)

# END CLASSIC_STRATEGY
