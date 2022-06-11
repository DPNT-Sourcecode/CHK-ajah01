# noinspection PyUnusedLocal
# skus = unicode string
items = {'A': 50,
         'B': 30,
         'C': 20,
         'D': 15,
         }


def checkout(skus):
    total = 0
    countA = 0
    countB = 0

    if len(skus) == 0:
        return 0
    for x in range(0, len(skus)):
        if x != 'A' or x != 'B' or x != 'C' or x != 'D':
            return -1


    for key, val in items.items():
        for y in range(0, len(skus)):
            if key == skus[y]:
                if key == 'A':
                    countA += 1
                if key == 'B':
                    countB += 1
                total += val
                if countA == 3:
                    total -= 20
                    countA = 0
                if countB == 2:
                    total -= 15
                    countB = 0
    return total





