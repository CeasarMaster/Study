import os

with open(os.path.abspath('first_tour.txt'), encoding='UTF-8', mode='r') as file:
    strings = file.read().split('\n')
    pass_score = int(strings.pop(0))
    scores={}

    for i in strings:
        n=i.split()
        scores[n[0]+n[1]]=n[2]
    print(scores)

