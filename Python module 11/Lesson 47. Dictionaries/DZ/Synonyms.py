synonyms = dict()
x = int(input('Insert the amount of pairs: '))
for i in range(x):
    n = input('Insert the synonyms: ').split()
    synonyms[n[0]] = n[1]
while True:
    y = input('Insert the word: ').lower()

    if y.title() not in synonyms.keys() and y.title() not in synonyms.values():
        print('Word is not in dictionary')

    else:
        for i in synonyms:
            if y == i.lower():
                print(f'Synonym: {synonyms[i]}')
                break
            if y == synonyms[i].lower():
                print(f'Synonym: {i}')
                break
'''Привет Здравствуйте
Insert the synonyms: Печально Грустно'''
