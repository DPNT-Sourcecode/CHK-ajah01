

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
        for y in range (0, len(skus)):
            if i == skus[y]:
                
        total += i
    return total





