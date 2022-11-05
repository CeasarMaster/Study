def gamble(cash):
    n = int(input('Insert the number on the cube: '))
    if cash >= 10000:
        print('Game Over')
        return cash
    if n == 3:
        print('You lost everything ')
        print('Game Over')
        cash = 0
        return cash
    else:
        print('You won 500 rubles!')
        cash+=500
        return gamble(cash)

money = int(input('Insert the started balance: '))
print(gamble(money))

'''money = int(input('Insert the starter balance: '))
while True:
    if money < 10000:
        n = int(input('What number is on the cube: '))
    if money >= 10000:
        print('Game over!')
        print(money)
        break
    if n == 3:
        print('You lost everything!')
        print('Game over!')
        money = 0
        print(money)
        break
    else:
        print('You won 500 rubles!')
        money += 500'''
