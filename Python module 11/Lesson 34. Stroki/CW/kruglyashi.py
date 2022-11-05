n = input('Insert a number bigger than 100: ')
counter = 0
x = ['6', '9', '0']
for i in n:
    if i in x:
        counter += 1
    if i == '8':
        counter += 2
print('kruglyashi=', counter)
