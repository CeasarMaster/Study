symbols = '@', '№', '$', '%', '^', '&', '*', '(', ')'
file = '.txt', '.docx'
print(symbols)
print(file)
n = input('Insert the file name: ')
if n.startswith(symbols) or not n.endswith(file):
    print('File name incorrect...')
else:
    print('File name correct...')

