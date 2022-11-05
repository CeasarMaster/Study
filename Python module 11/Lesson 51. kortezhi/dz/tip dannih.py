n = {'h': 1, 'e': 2, 'l': 3, 'o': 4, }


def iterable(n):
    x = []
    for i, j in enumerate(n):
        if i % 2 == 0:
            if isinstance(n, dict):
                x.append([j, n[j]])
            else:
                x.append(j)
    return x


print(iterable(n))
