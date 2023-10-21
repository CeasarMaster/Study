N = []
x = int(input('Insert the amount of dogs participating: '))
for i in range(x):
    y = int(input('Insert the results: '))
    N.append(y)
print(N)
k = N.index(min(N))
g = N.index(max(N))
N[k], N[g] = N[g], N[k]
print(N)
