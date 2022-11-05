n = input('Insert something: ')
z = ''
for i in n:
    z = i + z
if n == z:
    print('Word is palindrome')
else:
    print('Not a palindrome')
