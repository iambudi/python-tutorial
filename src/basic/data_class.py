from dataclasses import dataclass
from datetime import datetime
from typing import List

"""
Data Class:
decorator and functions for automatically adding generated special 
methods such as __init__() and __repr__() to user-defined classes.
For simple data structure its encourages to use dict or named tuple
"""


@dataclass(frozen=True)  # frozen true means immutable
class OrderItem:
    # by default, if not using kwargs, constructor args 
    # follow the order of class attribute declaration below
    # OrderItem(1, "prod id", "1", "PCS" .. so on)
    id: int
    product: str
    qty: int
    uom: str
    price: float
    discount: float
    amount: float


@dataclass
class SalesOrder:
    # slots is optional used to restrict what is allowed
    # to be defined as class attribute. If we just put 'id' in slot list
    # it will throw: object has no attribute 'order_date'
    # __slots__ = ['id', 'order_date', 'customer', 'items', 'currency']
    id: int
    order_date: datetime
    customer: str
    items: List[OrderItem]  # class OrderItem must be declared first before used
    currency: str = "IDR"  # specify default value

    def calculate_total(self) -> float:
        amount = 0.00
        for item in self.items:
            amount += item.amount
        return amount

    def eligible_for_coupon(self) -> bool:
        return self.calculate_total() >= 100000


# with dataclass decorator, we no longer need to create __init__ method
# to declare constructor args
order = SalesOrder(id=1, order_date=datetime.now(), customer="Mr. Wick", items=[])
order.items.append(OrderItem(1, "Roasted Coffee Beans 500gr", 2, "pack", 100000, 20000, 80000))
order.items.append(OrderItem(1, "Dairy Milk 1lt", 1, "pack", 22000, 0, 20000))

print(f"New order from {order.customer} with {len(order.items)} items in total {order.currency} {order.calculate_total()}")
print(f"{order.customer} eligible for discount coupon? {order.eligible_for_coupon()}")

# Check dataclass frozen=True/immutability
items = OrderItem(1, "Choco Banana Snack", 1, "PCS", 20000, 0, 2000)
# items.discount = 1000 # error Cannot assign member "discount" for type "OrderItem"

# dataclass by default implements __repr__() method
print("Order:", order)


@dataclass  # setting frozen=True not allowed if inherit from a class that is not frozen
class Billing(SalesOrder):
    """
    Dataclass can be inherited freely like regular class
    when last parent attribute contains default value
    the subclass attribute must then specify value as well
    remove the default below to see it
    """

    top: int = 0  # term of payment. will be at the end of constructor args


# attributes automatically inherits from its parent
billing = Billing(id=1, order_date=datetime.now(), customer="Another Customer", items=[], currency="USD", top=7)
print(billing)
