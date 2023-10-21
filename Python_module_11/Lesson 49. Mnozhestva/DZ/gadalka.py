n = int(input('Insert the maximum number: '))
user_number2 = set(range(1, n + 1))

while True:

    user_number = input('Insert the string: ')
    if user_number == 'Help!':
        print('Artem could have these numbers in mind: ', user_number2)
        break
    else:
        user_number = set([int(i) for i in user_number.split()])
        artem = input('Answer of Artem: ').lower()
        if artem == 'yes':
            user_number2.intersection_update(user_number)

        else:
            user_number2.difference_update(user_number)
