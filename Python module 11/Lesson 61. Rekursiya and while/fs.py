n = int(input('Insert the number: '))
total = 0
while True:
    total += n // 10 ** (len(str(n)) - 1)
    n %= 10 ** (len(str(n)) - 1)
    if n // 10 ** (len(str(n)) - 1) == 5:
        print('Boom')
        break

    if n == 0:
        break
print(total)
