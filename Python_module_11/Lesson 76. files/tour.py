import os

with open(os.path.abspath('first_tour.txt'), encoding='UTF-8', mode='r') as file, open(
        os.path.abspath('second_tour.txt'), encoding='UTF-8', mode='w') as file2:
    strings = file.read().split('\n')
    pass_score = int(strings.pop(0))
    scores = {}

    for i in strings:
        n = i.split()
        scores[f'{n[0]}  {n[1]}'] = int(n[2])
    scores_list = sorted(scores, key=lambda a: scores[a], reverse=True)
    results = []
    for j, i in enumerate(scores_list):
        if scores[i] > 80:
            surname, name = i.split()
            results.append(f'{j + 1}) {name[0]}. {surname} {scores[i]}')
    file2.write('\n'.join(results))
