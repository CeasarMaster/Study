'''n = input('Insert a message: ').split(',')
print(n)
print(','.join(n))
n = ' '.join(n)
print(n.upper())
print(n.lower())
z = '123.txt'
if z.endswith('.txt'):
    print('ok')
else:
    print('false')
if z.startswith('123'):
    print('ok')
else:
    print('false')'''

'''words = input('Insert the words: ').split()
text = input('Insert the text: ').split()
for i in words:
    print('word: {} amount: {}'.format(i, text.count(i)))'''

'''text = input('Insert the text: ').split()
text = ' '.join(text)
print(text)'''

names = input('Insert the names: ').split(',')
ages = input('Insert the ages: ').split()
print(ages)
shablon = input('Insert the message: ')
for i in range(len(names)):

    print(shablon.format(name=names[i], age=ages[i]))
