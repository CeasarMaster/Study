phone_book = {}
while True:
    print('1. Add contact')
    print('2. Find person')
    n = int(input('Insert the action: '))

    if n == 1:

        name = input('Insert the name and surname of contact: ').split()
        number = int(input('Insert the number: '))
        if tuple(name) in phone_book:
            print('The person is already in your contacts.')
        else:
            phone_book[(name[0], name[1])] = number
        print(phone_book)
    if n == 2:
        search = input('Insert the surname for searching: ')
        for i in phone_book:
            if search == i[1]:
                print(i, phone_book[i])
