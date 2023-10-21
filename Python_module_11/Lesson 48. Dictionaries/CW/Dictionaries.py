'''n = {'Hello': 'World', 'apples': 'bananas', 'red': 'green'}
for i,j in n.items():
    print(i,j)'''

'''incomes = {

    'apple': 5600.20,

    'orange': 3500.45,

    'banana': 5000.00,

    'bergamot': 3700.56,

    'durian': 5987.23,

    'peach': 10000.50,

    'pear': 1020.00,

    'persimmon': 310.00,

}

for i,j in incomes.items():
    print(f'{i} -- {j}')'''

server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i, j in server_data.items():
    print(i)
    for x, y in j.items():
        print('\t', x, y)
