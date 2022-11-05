x = input('Insert the string: ')
string_1 = set(x)
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
string_1.intersection_update(numbers)
print(''.join(sorted(string_1)))
