counter1 = 0
counter2 = 0
total_coins = []

coins = int(input())
for i in range(coins):
    n = int(input())
    total_coins.append(n)

for j in total_coins:
    if j == 1:
        counter1 += 1
    if j == 0:
        counter2 += 1
if counter1 > counter2:
    print(counter2)
if counter2 > counter1:
    print(counter1)
