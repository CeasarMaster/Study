import os


def calculate(expression):
    try:
        n1 = int(expression[0])
        operator = expression[1]
        n2 = int(expression[2])
        results = 0

        if operator == '+':
            results = n1 + n2
        elif operator == '-':
            results = n1 - n2
        elif operator == '*':
            results = n1 * n2
        elif operator == '/':
            results = n1 / n2
        else:
            raise ValueError
        return results
    except ValueError as incorrect_value:
        return None


with open(os.path.abspath('calc.txt'), encoding='UTF-8', mode='r') as file:
    summa = 0
    for i in file:
        n = i.split()
        x = calculate(n)
        if x is not None:
            summa += x
        else:
            print('Something went wrong in string:', ' '.join(n))
            change = input('Would you like to change this expression? ')
            if change == 'yes'.lower():
                while True:
                    new_expr = input('Insert the new expression: ').split()
                    x = calculate(new_expr)
                    if x is not None:
                        summa += x
                        break

    print(summa)
