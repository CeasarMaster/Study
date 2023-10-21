tiles = []

for _ in range(3):
    n = input()
    tiles.append(n)

char = ''
if tiles[0][0] == tiles[1][1] == tiles[2][2]:
    char = tiles[0][0]
elif tiles[0][2] == tiles[1][1] == tiles[2][0]:
    char = tiles[0][2]
elif tiles[0][0] == tiles[0][1] == tiles[0][2]:
    char = tiles[0][0]
elif tiles[1][0] == tiles[1][1] == tiles[1][2]:
    char = tiles[1][0]
elif tiles[2][0] == tiles[2][1] == tiles[2][2]:
    char = tiles[2][0]
elif tiles[0][0] == tiles[1][0] == tiles[2][0]:
    char = tiles[0][0]
elif tiles[0][1] == tiles[1][1] == tiles[2][1]:
    char = tiles[0][1]
elif tiles[0][2] == tiles[1][2] == tiles[2][2]:
    char = tiles[0][2]

if char == 'X':
    print('Win')
elif char == 'O':
    print('Lose')
else:
    print('Draw')
