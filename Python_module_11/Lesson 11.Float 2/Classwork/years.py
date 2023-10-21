'''a = int(input('Insert the year: '))
b = int(input('Insert the year: '))
for i in range(a, b + 1):
    n1 = i // 1000
    n2 = i // 100 % 10
    n3 = i // 10 % 10
    n4 = i % 10
    if n1 == n2 and n1 == n3 or n1 == n3 and n1 == n4 or n2 == n3 and n2 == n4 or n1 == n2 and n1 == n4:
        print(i)'''

y = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a = int(input())
b = int(input())
for i in range(a, b + 1):
    for j in y:
        if str(i).count(j) == 3:
            print(i)
            break
