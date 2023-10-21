'''def password():
    n = int(input('Insert the password: '))
    if n == 235:
        return 'Correct password'
    else:
        print('Incorrect password. Try again.')
        return password()


print(password())'''

'''while True:
    n = int(input('Insert the password: '))
    if n == 235:
        print('Correct password! Welcome.')
        break
    else:
        print('Incorrect password. Try again')'''
'''counter = 0
while True:
    n = int(input('How much money to save: '))
    counter += n
    if counter >= 500000:
        print('New car!')
        break'''


def kopilka(counter):
    n = int(input('How much money to save: '))
    counter += n
    if counter >= 500000:
        return 'New Car!'
    else:
        return kopilka(counter)


c = 0
print(kopilka(c))
