countries = dict()
n = int(input('Insert the amount of countries: '))
for i in range(n):
    x = input(f'{i + 1} country: ').split()
    countries[x[0]] = x[1:]
for i in range(3):
    c = input(f'{i + 1} city: ')
    for j in countries:
        if c in countries[j]:
            print(f'City {c} is located in {j}')
            break
    else:
        print(f'There is no data on the city {c}')
