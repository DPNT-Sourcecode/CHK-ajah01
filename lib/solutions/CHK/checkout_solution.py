

# noinspection PyUnusedLocal
# skus = unicode string
items = {'A': {'price': 50},
         'B': {'price': 30},
         'C': {'price': 20},
         'D': {'price': 15},
         }


def checkout(skus):
    total = 0
    for i in items:
        total += i
    return total


