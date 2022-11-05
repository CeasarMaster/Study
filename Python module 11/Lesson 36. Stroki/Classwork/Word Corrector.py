n = input().split()
position = int(n[0])
word = n[1]
print(word[:position-1]+word[position:])
