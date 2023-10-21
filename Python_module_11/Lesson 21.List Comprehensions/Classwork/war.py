import random as r

first_squad = [r.randint(50, 80) for _ in range(10)]
second_squad = [r.randint(30, 60) for _ in range(10)]
result = ['Выжил' if first_squad[i] + second_squad[i] < 100 else 'Погиб' for i in range(10)]
print(first_squad)
print(second_squad)
print(result)
