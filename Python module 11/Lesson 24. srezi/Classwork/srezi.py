'''n = input('Insert the text: ')
first = n.index('h')
counter = 0
counter2 = 0
h = n.count('h')
for i in n:
    counter2 += 1
    if i == 'h':
        counter += 1
        if counter == h:
            break
print(n[counter2-2:first:-1])'''

n = input('Insert the text: ')
first = n.index('h')
n = n[first + 1:]
n = n[::-1]
first = n.index('h')
n = n[first + 1:]
print(n)
