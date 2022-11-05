players = {

    ("Ivan", "Volkin"): (10, 5, 13),

    ("Bob", "Robbin"): (7, 5, 14),

    ("Rob", "Bobbin"): (12, 8, 2)

}
n = []
for key, value in players.items():
    n.append((key + value))
print(n)
