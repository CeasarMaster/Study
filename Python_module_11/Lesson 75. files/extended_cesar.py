import cesar_functions

user_choice = input('Code or Decode string? ').lower()
user = input('Insert the string: ')
step = int(input('Insert the step: '))
lang = 'rus' if all([i in cesar_functions.alphabet_rus for i in user.lower() if i.isalpha()]) else 'eng'

if user_choice == 'code':
    coded_string = cesar_functions.coder(step, user, lang)
    print(coded_string)

if user_choice == 'decode':
    decoded_string = cesar_functions.decoder(step, user, lang)
    print(decoded_string)
