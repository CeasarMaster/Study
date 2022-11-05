a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
print('The amount of elements 5 is:', a.count(5))
for j in a:
    if j == 5:
        a.remove(j)
a.extend(c)
print('The amount of elements 3 is:', a.count(3))
print(a)

