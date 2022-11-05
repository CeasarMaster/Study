letters = ['A', 'B', 'C', 'E', 'H', 'K', 'M', 'O', 'P', 'T', 'X', 'Y']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while True:
    counter = 0
    x = input('Insert the number plate: ')
    for i in range(6):
        if x[i] in letters and i == 0 or i > 3 and x[i] in letters:
            counter += 1
        if x[i] in numbers and 0 < i < 4:
            counter += 1

    if counter == 6:
        print('Yes')
    else:
        print('No')
