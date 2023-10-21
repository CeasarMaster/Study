m1, m2, m3 = map(int, input().split())
weight = [m1, m2, m3]

for i in weight:
    if i < 94 or i > 727:
        print('Error')
        break
else:
    print(max(weight))
