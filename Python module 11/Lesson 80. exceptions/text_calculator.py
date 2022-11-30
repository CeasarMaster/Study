import os


def calculate(expression):
    try:
        n1 = int(expression[0])
        operator = expression[1]
        n2 = int(expression[2])
        results = 0

        if operator == '+':
            results = n1 + n2
        if operator == '-':
            results = n1 - n2
        if operator == '*':
            results = n1 * n2
        if operator == '/':
            results = n1 / n2
        return results
    except ValueError as incorrect_value:
        return 0


with open(os.path.abspath('calc.txt'), encoding='UTF-8', mode='r') as file:
    summa = 0
    for i in file:
        n = i.split()
        x = calculate(n)
        summa += x
        if x == 0:
            print('Something went wrong')
    print(summa)
