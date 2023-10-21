n = [1, 2, 3, 4, 5]
n2 = []
k = int(input('Insert the amount of indexes you want the numbers to move: '))
k *= (-1)
for _ in range(len(n)):
    n2.append(n[k])
    k += 1
print(n2)
