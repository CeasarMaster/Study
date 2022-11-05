'''n = [i ** 2 for i in range(20) if i % 2 == 0]
print(n)'''

'''n = [i ** 2 if i % 2 == 0 else i ** 3 for i in range(20)]
print(n)'''

import random as r

'''n = [r.randint(1, 100) for _ in range(10)]
print(n)'''


def reverse_num(n):
    n = str(n)
    n2 = ''
    for i in n:
        n2 = i + n2
    return int(n2)


reverse = [reverse_num(r.randint(1, 100)) for _ in range(100)]
print(reverse)
reverse2 = [reverse_num(i) for i in reverse]
print(reverse2)
print(sum(reverse2))