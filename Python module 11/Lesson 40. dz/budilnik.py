s, t = map(int, input().split())
if t < s:
    c = 12 - s + t
else:
    c = t - s
print(c)
