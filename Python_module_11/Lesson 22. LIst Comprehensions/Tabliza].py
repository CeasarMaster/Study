import random

team1 = [(round(random.uniform(5, 10), 2)) for _ in range(20)]
team2 = [(round(random.uniform(5, 10), 2)) for _ in range(20)]
winners = [team1[i] if team1[i] > team2[i] else team2[i] for i in range(20)]
print(team1)
print(team2)
print(winners)
