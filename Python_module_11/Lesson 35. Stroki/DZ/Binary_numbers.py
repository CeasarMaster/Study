n = abs(int(input()))
binary = 1
while binary <= n:
    binary *= 2
    if binary == n:
        print('YES')
        break
else:
    print('NO')
