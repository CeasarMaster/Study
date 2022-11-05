factorials = {1: 1}


def calculating_math_func(data):
    max_keys = max(factorials.keys())
    if data > max_keys:
        result = factorials[max_keys]

        for index in range(max_keys + 1, data + 1):
            result *= index
            factorials[index] = result

    else:
        result = factorials[data]
    '''result /= data ** 3
    result = result ** 10'''
    return result


while True:
    n = int(input('Insert a number: '))
    print(n, calculating_math_func(n))
