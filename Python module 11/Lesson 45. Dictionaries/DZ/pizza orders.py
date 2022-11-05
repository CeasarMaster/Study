n = int(input('Insert the amount of orders: '))
orders = dict()
for i in range(n):
    x = input('Insert the name, type of pizza and amount: ').split()
    if x[0] not in orders:
        orders[x[0]] = {x[1]: int(x[2])}
    else:
        if x[1] in orders[x[0]]:
            orders[x[0]][x[1]] += int(x[2])
        else:
            orders[x[0]][x[1]] = int(x[2])

for i in orders:
    print(f'{i}:')
    for j in orders[i]:
        print(f'\t{j}:{orders[i][j]}')

'''Insert the name, type of pizza and amount: Иванов Пепперони 1
Insert the name, type of pizza and amount: Петров Де-Люкс 2
Insert the name, type of pizza and amount: Иванов Мясная 3
Insert the name, type of pizza and amount: Иванов Мексиканская 2
Insert the name, type of pizza and amount: Иванов Пепперони 2
Insert the name, type of pizza and amount: Петров Интересная 5'''