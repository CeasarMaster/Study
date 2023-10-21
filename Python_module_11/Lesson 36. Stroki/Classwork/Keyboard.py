n = input()
keys = 'qwertyuiopasdfghjklzxcvbnm'
x = (keys.index(n) + 1) % 26
print(keys[x])
