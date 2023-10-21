'''n = input('Insert a word: ')

counter = 0
for i in n:
    counter2 = 0
    for j in n:
        if i == j:
            counter2 += 1
    if counter2 == 1:
        counter += 1
print('number of unique letters: ', counter)'''

n = input('Insert a word: ')

counter = 0
for i in n:
    if n.count(i) == 1:
        counter += 1
print(counter)
