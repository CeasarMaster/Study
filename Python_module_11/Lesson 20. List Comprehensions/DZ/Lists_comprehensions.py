'''n1 = int(input('Insert the left border: '))
n2 = int(input('Insert the right border: '))
list1 = [i ** 2 for i in range(n1, n2 + 1)]
list2 = [i ** 3 for i in range(n1, n2)]
print(list1)
print(list2)'''

'''n = list(input('Insert the text:'))
n2 = input('Insert the additional symbol:')
list1 = [i * 2 for i in n]
list2 = [str(i) + n2 for i in list1]
print(list1)
print(list2)'''

n = [float(input('Insert the price:')) for _ in range(4)]
p1 = int(input('Повышение за первый год:')) / 100 + 1
p2 = int(input('Повышение за второй год:')) / 100 + 1
n2 = [i * p1 for i in n]
n3 = [i * p2 for i in n2]
print(sum(n), sum(n2), sum(n3))
