#
# try:
#     n = int(input('Insert a number: '))
#     n2 = int(input('Insert the 2nd number: '))
#     print(n / n2)
# except ValueError:
#     print('Something went wrong')
# except ZeroDivisionError:
#     print('Unable to divide by 0')
# else:
#     print('Everything Okay')
# finally:
#     print('Program closed')
#
try:
    n=input('Insert your name: ')

    if n=='Paul':
        raise ValueError('You are not allowed here!')
except ValueError as error:
    print(error)
