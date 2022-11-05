import os


def f(elem):
    return letters[elem]


with open(os.path.abspath('text.txt'), encoding='UTF-8', mode='r') as file:
    string = file.read().lower()
    counter = 0
    letters = {}
    for i in string:
        if i.isalpha():
            counter += 1
            letters[i] = string.count(i)

    for i in letters:
        letters[i] = round(letters[i] / counter, 3)

with open(os.path.abspath('analysis.txt'), encoding='UTF-8', mode='w') as file2:
    sorted_letters = sorted(letters, key=f, reverse=False)
    letters_lst = ''.join(letters.keys())
    numbers_lst = []
    for i in letters.values():
        numbers_lst.append(i)

    numbers_string=''
    for i in range(len(letters_lst)):
        numbers_string+=f'{letters_lst[i]} : {numbers_lst[i]}\n'
    file2.write(numbers_string)
