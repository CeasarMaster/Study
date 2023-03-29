import random

sign = ['rock', 'paper', 'scissors']
random_num = random.randint(0, 2)
chosen_sign = sign[random_num]
n = input('Rock, paper or scissors?: ')
if n == 'rock'.lower() and chosen_sign == 'paper':
    print(f'The bot chose paper. You lose!')

elif n == 'scissors'.lower() and chosen_sign == 'paper':
    print(f'The bot chose paper. You win!')

elif n == 'scissors'.lower() and chosen_sign == 'rock':
    print(f'The bot chose rock. You lose!')

elif n == 'paper'.lower() and chosen_sign == 'rock':
    print(f'The bot chose rock. You win!')

elif n == 'paper'.lower() and chosen_sign == 'scissors':
    print(f'The bot chose scissors. You lose!')

elif n == chosen_sign:
    print('DRAW!')
