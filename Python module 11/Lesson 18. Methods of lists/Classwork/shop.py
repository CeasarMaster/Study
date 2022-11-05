shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
n = input('Insert what do you want to buy: ')
counter = 0
summa = 0
for i in shop:
    if n in i:
        counter += 1
        summa = i[1] + summa
print('The amount of parts: ', counter)
print('The total price is: ', summa)
