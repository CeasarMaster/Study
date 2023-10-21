import os

with open(os.path.abspath('answers.txt'), encoding='UTF-8', mode='w') as answers, \
        open('numbers.txt', encoding='UTF-8',mode='r') as numbers:
    sum_num = 0
    for i in numbers:
        sum_num += int(i)
    answers.write(str(sum_num))
    numbers.close()
print(numbers.closed)
