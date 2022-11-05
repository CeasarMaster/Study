n_palok = int(input('Insert the amount of sticks: '))
palki = '|' * n_palok
print(palki)
n_broski = int(input('Insert the amount of shots: '))
for i_throw in range(n_broski):
    print('Throw', i_throw + 1)
    broski1 = int(input('Sticks taken down from number: '))
    broski2 = int(input('to number: '))
    palki = palki[:broski1 - 1] + '.' * (broski2 - broski1 + 1) + palki[broski2:]
    print(palki)
