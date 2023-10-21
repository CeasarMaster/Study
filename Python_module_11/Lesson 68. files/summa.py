import os

with open(os.path.abspath('answers2.txt'),encoding='UTF-8',mode='w') as answers:
    numbers=open('numbers2.txt',encoding='UTF-8')
    sum_num=0
    for i in numbers:
        sum_num+=int(i)
    answers.write(str(sum_num))
    numbers.close()


