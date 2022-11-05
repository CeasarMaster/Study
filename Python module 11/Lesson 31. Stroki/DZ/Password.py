counter = 0
counter_cap = 0
while True:

    password = list(input('Insert the password: '))

    for i in password:
        if i.isdigit():
            counter += 1
        if i.isupper():
            counter_cap += 1

    if counter < 3 or len(password) < 8 or counter_cap < 1:
        print('Password is insecure.Try again...')
    else:
        print('Secure')
        break
