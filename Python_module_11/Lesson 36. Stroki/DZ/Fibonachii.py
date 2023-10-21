n = int(input('Insert the number: '))
a = 1
b = 1
for _ in range(n - 2):
    c = a + b
    a = b
    b = c
print(c)
