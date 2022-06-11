# noinspection PyUnusedLocal
# skus = unicode string
items = {'A': 50,
         'B': 30,
         'C': 20,
         'D': 15,
         }


def checkout(skus):
    total = 0
    if len(skus) == 0:
        return -1

    for key, val in items.items():
        for y in range(0, len(skus)):
            if key == skus[y]:
                total += val
    return total





