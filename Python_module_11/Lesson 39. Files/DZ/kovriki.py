w, h, r = map(int, input().split())
if 2 * r <= min(w, h):
    print('YES')
else:
    print('NO')
