alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
message = input('Insert the message: ')
move = int(input('Insert the amount to move: '))
coded_message = ''
for i in message:
    if i in alphabet:
        current_place = alphabet.find(i)
        new_place = (current_place + move) % 33
        coded_message = '{first}{second}'.format(first=coded_message, second=alphabet[new_place])
    else:
        coded_message = f'{coded_message}{i}'

print(coded_message)
