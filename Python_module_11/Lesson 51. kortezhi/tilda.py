n = input('Insert the string: ')
for i, x in enumerate(n):
    if x == '~':
        print(i, end=' ')
