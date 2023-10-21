n = int(input('Insert the amount of friends:'))
k = int(input('Insert the amount of checks:'))
counter_money = [0 for _ in range(n)]
for i in range(1, k + 1):
    print(i, 'Check')
    n2 = int(input('To:'))
    n3 = int(input('From:'))
    total = int(input('How much:'))
    counter_money[n3 - 1] += total
    counter_money[n2 - 1] -= total
print('Balance:')
for j in range(n):
    print(j + 1, ':', counter_money[j])
