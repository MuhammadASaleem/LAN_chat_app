import random as np


def dice():
    first = np.random.choice([1, 2, 3, 4, 5, 6], size=(int(1e6), 1))
    second = np.random.choice([1, 2, 3, 4, 5, 6], size=(int(1e6), 1))
    merged = tuple(zip(first, second))
    count = 0
    for i in merged:
        if i[0] == i[1]:
            count += 1
    print((count / 1000000) * 100)


dice()
