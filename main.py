def calculate_balance(year):
    balance = 1000.0
    for _ in range(2010, year):
        balance += balance * 0.04
        balance += 1000.0

    return balance


for i in range(2010, 2050):
    balance = calculate_balance(i)
    print(f'{i}: ${balance:,.2f}')
    if balance >= 50000.00:
        break


# from datetime import datetime

# current_time = datetime.now()

# print(f'{current_time.day}/{current_time.month}/{current_time.year}')
# print(f'{current_time.hour}:{current_time.minute}')