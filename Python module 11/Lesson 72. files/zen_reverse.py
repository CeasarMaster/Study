import os

with open(os.path.abspath('zen.txt'),encoding='UTF-8',mode='r') as file:
    x=file.readlines()
    x.reverse()
    print(''.join(x))