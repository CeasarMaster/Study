def tpl_sort(tpl):
    for i in tpl:
        if isinstance(i, float):
            return tpl
        else:
            return tuple(sorted(tpl))


n = (6, 3, -1, 8, 4, 10, -5)

print(tpl_sort(n))
