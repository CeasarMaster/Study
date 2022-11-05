n = input('Insert the text: ')
n = n.split()
word = ''
counter = 0
for i in n:
    if len(i) > counter:
        counter = len(i)
        word = i
print(word)
print(counter)

