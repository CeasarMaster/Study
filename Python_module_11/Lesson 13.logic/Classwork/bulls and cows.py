import random

p = str(random.randint(1000, 9999))
while True:
    v = input('Insert the second number: ')
    bulls = 0
    cows = 0
    if p == v:
        print('You guessed the number')
        print('the number was: ', p)
        break
    for i in range(4):

        if p[i] == v[i]:
            bulls += 1
            continue
        if p[i] in v:
            cows += 1

    print('number of bulls: ', bulls)
    print('number of cows: ', cows)
