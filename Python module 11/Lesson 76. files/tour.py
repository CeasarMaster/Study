import os

with open(os.path.abspath('first_tour.txt'), encoding='UTF-8', mode='r') as file, open(
        os.path.abspath('second_tour.txt'), encoding='UTF-8', mode='w') as file2:
    strings = file.read().split('\n')
    pass_score = int(strings.pop(0))
    scores = {}

    for i in strings:
        n = i.split()
        scores[f'{n[0]}  {n[1]}'] = int(n[2])
    print(scores)

    for i in scores:
        if scores[i] > 80:
            surname, name = i.split()
            file2.write('\n'f'{name[0]}. {surname} {scores[i]}')
