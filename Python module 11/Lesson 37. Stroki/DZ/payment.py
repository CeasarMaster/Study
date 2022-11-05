n = []
for i in range(3):
    x = int(input())
    n.append(x)
minimum = min(n)
maximum = max(n)
result = maximum - minimum
print(result)
