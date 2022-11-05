numbers = dict()

while True:
    print('Current contacts in phone book: ')

    for i in numbers:
        print(i, numbers[i])

    name = input('Insert the name: ')

    if name in numbers:
        print('Error name already in the phone book.')
        continue
    phone = int(input('Insert the phone: '))
    numbers[name] = phone
