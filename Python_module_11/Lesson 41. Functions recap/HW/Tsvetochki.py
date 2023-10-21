g = 'G'
c = 'C'
v = 'V'
x = ''
n = int(input())
for i in range(n):
    x = v
    v = c
    c = x
    x = g
    g = c
    c = x
print(g+c+v)
