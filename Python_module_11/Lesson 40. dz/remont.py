l, w, h = map(int, input().split())
n = (l * h + w * h) * 2
if n % 16 == 0:
    n = n // 16
else:
    n = n // 16 + 1
print(n)
