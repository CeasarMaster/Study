incomes = {

    'apple': 5600.20,

    'orange': 3500.45,

    'banana': 5000.00,

    'bergamot': 3700.56,

    'durian': 5987.23,

    'grapefruit': 300.40,

    'peach': 10000.50,

    'pear': 1020.00,

    'persimmon': 310.00,

}
sums = incomes['apple']
for i, j in incomes.items():
    if j < sums:
        sums = j
        x = i

print('Total income=', sum(incomes.values()))
print('Minimum income is of', x, min(incomes.values()))
incomes.pop(x)
print(incomes)
