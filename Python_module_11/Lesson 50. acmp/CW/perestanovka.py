n = input().split()
n = [int(i) for i in n]
if n[0] + n[1] == n[2]:
    print('YES')
elif n[1] + n[2] == n[0]:
    print('YES')
elif n[0] + n[2] == n[1]:
    print('YES')
else:
    print('NO')
