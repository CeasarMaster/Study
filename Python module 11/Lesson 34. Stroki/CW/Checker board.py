coordinate = input('Insert the coordinate: ')
letters = ['B', 'D', 'F', 'H']
letters2 = ['A', 'C', 'E', 'G']
if coordinate[0] in letters and int(coordinate[1]) % 2 != 0 or coordinate[0] in letters2 and int(coordinate[1]) % 2 == 0:
    print('WHITE')
else:
    print('BLACK')
