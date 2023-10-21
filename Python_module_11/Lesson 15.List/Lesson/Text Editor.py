'''s = input('Insert text: ')
counter = 0
n = list(s)
for i in n:
    if ':' == i:
        counter += 1
        n[n.index(i)] = ';'
print('Number of changes:', counter)
print(n)'''

'''s = input('Insert text: ')
counter = 0
x = ''
for i in s:
    if ':' == i:
        counter += 1
        x += ';'
        continue
    x += i


print('Number of changes:', counter)
print(x)'''

s = input('Insert text: ')
counter = s.count(':')
s = s.replace(':', ';', counter)

print('Number of changes:', counter)
print(s)
