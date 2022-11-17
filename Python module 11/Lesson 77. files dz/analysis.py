import os

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
    letters_list = ''.join(letters.keys())
    numbers_list = []
    for i in letters.values():
        numbers_list.append(i)
    numbers_string = ''
    for i in range(len(letters_list)):
        numbers_string = f'{letters_list[i]} : {numbers_list[i]}\n'
        file2.write(numbers_string)
