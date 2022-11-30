import os

# try:
#     BRUCE_WILLIS = 42
#
#     input_data = input('Введите строку: ')
#
#     leeloo = int(input_data[4])
#
#     result = BRUCE_WILLIS * leeloo
#
#     print(f'- Leeloo Dallas! Multi-pass № {result}!')
# except ValueError:
#     print('невозможно преобразовать к числу')
# except IndexError:
#     print('выход за границы списка')

with open(os.path.abspath('people.txt'), encoding='UTF-8', mode='r') as file, open(os.path.abspath('errorslog.txt'),
                                                                                   encoding='UTF-8',
                                                                                   mode='w') as file2:
    counter = 0

    for i in file.read():
        try:

            if i != '\n':

                counter += 1
                if len(i) < 3:
                    raise ValueError('Not enough symbols')
        except ValueError as error:
            n = error
    print(n)

    print(counter)
