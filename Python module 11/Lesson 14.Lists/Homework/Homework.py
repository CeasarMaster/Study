n = []
k = int(input('Insert the amount of numbers in the list: '))
for i in range(k):
    x = int(input('Insert the number: '))
    n.append(x)
g = int(input('Insert the divider: '))
y = 0
for z in n:
    if z % g == 0:
        y = y + n.index(z)
print('Sum of indexes:',y)
