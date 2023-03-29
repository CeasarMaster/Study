import time

y1 = int(input('Insert the first y-coordinate: '))
y2 = int(input('Insert the second y-coordinate: '))
x1 = int(input('Insert the first x-coordinate: '))
x2 = int(input('Insert the second x-coordinate: '))
print('Calculating gradient...')
time.sleep(1)
gradient = (y2 - y1) / (x2 - x1)
print(f'The gradient is: {gradient}')
