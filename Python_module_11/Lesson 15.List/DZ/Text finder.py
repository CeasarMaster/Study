n = input('Insert word 1: ')
n2 = input('Insert word 2: ')
n3 = input('Insert word 3: ')
words = []
words.append(n)
words.append(n2)
words.append(n3)
text = []
while True:
    word = input('Insert the words from the text: ')

    if word == 'end':
        break
    text.append(word)

for i in words:
    print(i, '-', text.count(i))
