code = list(input('Insert a string with 0 and 1 symbols: '))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
new_text = []
counter = 0
for i in code:
    if i == '0':
        counter += 1
    if i == '1':
        new_text.append(letters[counter])
        counter = 0

print(''.join(new_text))
