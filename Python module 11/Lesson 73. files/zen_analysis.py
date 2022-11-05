import os

with open(os.path.abspath('zen.txt'), encoding='UTF-8', mode='r') as file:
    counter_words = 0
    counter_letters = 0
    counter_strings = 0
    string_lst = file.readlines()
    letters={}


    for i in string_lst:
        if len(i)>1:
            counter_strings+=1


        for x in i:

            if x.isalpha():
                counter_letters += 1
            if x == ' ':
                counter_words += 1
    n=''.join(string_lst).lower()
    for i in n :
        if i.isalpha():
            letters[i]=n.count(i)
    for i in letters:
        minimum=min(letters.values())
        if minimum==letters[i]:
            print(i)





    print(counter_letters)
    print(counter_words)
    print(counter_strings)

