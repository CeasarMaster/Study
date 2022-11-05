'''def slicer(tpl, num):
    if tpl.count(num) == 1:
        y = tpl.index(num)
        return tpl[y:]
    if tpl.count(num) >= 2:
        y = tpl.index(num)
        y2 = list(tpl[:])
        y2.pop(y)
        y3 = y2.index(num) + 1
        return tpl[y:y3 + 1]
    if tpl.count(num) == 0:
        return tuple()'''


def slicer(tpl, num):
    n = []
    for i, j in enumerate(tpl):
        if j == num:
            n.append(i)
        if len(n) == 2:
            return tpl[n[0]:n[1] + 1]
    if len(n) == 1:
        return tpl[n[0]:]
    else:
        return tuple()


n = int(input())
x = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
print(slicer(x, n))
