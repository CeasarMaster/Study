n_palok = int(input('Insert the amount of sticks: '))
palki = list('|' * n_palok)
print(palki)
broski = int(input('Insert the amount of shots: '))
for i in range(1, broski + 1):
    print('Throw', i)
    brosok1 = int(input('Sticks shot down from: '))
    brosok2 = int(input('to:'))
    palki[brosok1 - 1:brosok2] = ['.' for _ in range(brosok1, brosok2 + 1)]
    print(' '.join(palki))
