n, m = map(int, input().split())
x = n // m
if n % m == 0:
    print((str(x)+' ') * m)
else:
    for i in range(m):
        if i == m - 1:
            print(n)
        else:
            print(x, end=' ')
            n -= x
