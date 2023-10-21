'''n = int(input('Insert a number: '))
x = []
for i in range(1, n + 1):
    if i % 2 == 1:
        x.append(i)
print(x)
x = list(range(1, n + 1, 2))'''

print(list(range(1, int(input('Insert the number: ')) + 1, 2)))
