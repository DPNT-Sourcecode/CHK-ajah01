# noinspection PyUnusedLocal
# skus = unicode string
items = {'A': 50,
         'B': 30,
         'C': 20,
         'D': 15,
         'E': 40,
         }


def checkout(skus):
    total = 0
    countA = 0
    countB = 0
    countE = 0

    if len(skus) == 0:
        return 0

    for y in range(0, len(skus)):
        if skus[y] in items:
            for key, val in items.items():
                if key == skus[y]:
                    if key == 'A':
                        countA += 1
                    if key == 'B':
                        countB += 1
                    if key == 'E':
                        countE += 1
                    total += val
        else:
            total = -1
            break
    if countA % 3 == 0:
        total -= 20 * (countA/3)
    else: total -= 20 * ()
    if countB >= 1:
        if countE == 2:
            total -= 30
        if countB % 2 == 0:
            total -= (15 * countB/2)
            if countE == 2:
                total -= 30

    return total


