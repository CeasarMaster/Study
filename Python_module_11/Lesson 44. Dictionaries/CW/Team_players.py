team_a = []
team_b = []
team_c = []

players_dict = {

    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},

    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},

    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},

    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},

    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},

    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},

    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},

    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}

}

for i in players_dict.values():
    if i['team'] == 'A' and i['status'] == 'Rest':
        team_a.append(i['name'])
    if i['team'] == 'B' and i['status'] == 'Training':
        team_b.append(i['name'])
    if i['team'] == 'C' and i['status'] == 'Travel':
        team_c.append(i['name'])
print(' '.join(team_a))
print(' '.join(team_b))
print(' '.join(team_c))
