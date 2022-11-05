n = int(input())
word = list(input())
for i in word:
    if word.index(i) == n:
        word.remove(i)
print(''.join(word))
