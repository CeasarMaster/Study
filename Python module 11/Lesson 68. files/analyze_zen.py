import os


def letters_count():
    pass


counter_letters = 0
counter_words = 0
counter_strings = 0

with open(os.path.abspath('zen.txt'), encoding='UTF-8', mode='r') as file:
    for i in file:
        n = i.split()
        for z in n:
            counter_words += 1 if any([x.isalpha() for x in z]) else 0

        counter_letters += len(i)
        counter_strings += 1 if len(i) > 2 else 0
    print(counter_letters)
    print(counter_strings)
    print(counter_words)
    file_read=file.read()
    alpha_set = set([i for i in file_read])
    letters_dict = dict(zip(alpha_set,[file_read.count(i) for i in alpha_set]))
    print(letters_dict)
    print(alpha_set)
with open(os.path.abspath('zen.txt'), encoding='UTF-8', mode='r') as file2:
    alpha_list=[chr(i) for i in range(ord('a'),ord('z')+1)]
    text=file2.read().lower()
    dictionary=dict(zip(alpha_list,[text.count(i) for i in alpha_list]))
    print(dictionary)
    print(sum(dictionary.values()))