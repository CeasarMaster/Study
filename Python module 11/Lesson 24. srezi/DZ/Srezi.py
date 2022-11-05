import random

n = int(input('Insert the amount of numbers in list: '))
numbers = [random.randint(0, 2) for _ in range(n)]
print(numbers)
for i in numbers:
    if i == 0:
        indexes = numbers.index(i)
        element = numbers.pop(indexes)
        numbers.append(element)
indexes = numbers.index(0)

print(numbers[:indexes])
