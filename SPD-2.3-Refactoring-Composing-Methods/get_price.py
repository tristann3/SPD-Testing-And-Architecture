# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace temporary variable with extracted method/query

# Code snippet. Not runnable.

def get_price():
    base_price = quantity * item_price
    discount_factor = 0
    if base_price > 1000:
        discount_factor = 0.95
    else:
        discount_factor = 0.98
    return base_price * discount_factor

def get_quantity():
  return quantity

def get_item_price():
  return item_price

def get_base_price():
  return get_quantity() * get_item_price()
