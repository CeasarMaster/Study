n = list(input('Insert the text: '))
letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
updated_letters = [i for i in n if i in letters]
print(updated_letters)
print('Length:', len(updated_letters))
