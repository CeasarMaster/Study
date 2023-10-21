import os

with open(os.path.abspath('zen.txt'),encoding='UTF-8',mode='r') as file:
    s=file.readlines()
    print(s)
    s.reverse()
    print(''.join(s))
