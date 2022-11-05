tiles = []
x = True
for i in range(4):
    n = input('Insert the  tiles:')
    tiles.append(n)
for i in range(3):
    for j in range(3):
        if tiles[i][j] == tiles[i + 1][j] == tiles[i][j + 1] == tiles[i + 1][j + 1]:
            print('No')
            x = False
            break
if x:
    print('Yes')
