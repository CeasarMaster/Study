start = int(input('Insert the starting amplitude: '))
stop = float(input('Insert the stoping amplitude: '))
counter = 0
while start > stop:
    start *= 1 - 0.084
    counter += 1
print(counter)
