n = int(input('Insert a number: '))
n_list = [1 if i % 2 == 0 else i % 5 for i in range(n)]
print(n_list)

