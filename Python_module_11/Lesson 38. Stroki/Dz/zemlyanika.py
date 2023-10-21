x, y, z = map(int, input().split())
answer = x + y - z
if answer >= 0:

    print(answer)
else:
    print('Impossible')
