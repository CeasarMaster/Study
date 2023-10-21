n = input()
counter = 0
for i in range(len(n)-4):
    x = n[i] + n[i + 1] + n[i + 2] + n[i + 3] + n[i + 4]
    if x == '>>-->' or x == '<--<<':
        counter += 1
print(counter)
