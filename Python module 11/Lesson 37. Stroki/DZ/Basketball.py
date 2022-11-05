team1 = 0
team2 = 0

for i in range(4):
    a, b = map(int, input().split())
    team1 = team1 + a
    team2 = team2 + b
if team1 > team2:
    print('1')
if team1 < team2:
    print('2')
if team1 == team2:
    print('DRAW')
