import random
def main_menu():
    rooms=['bedroom','kitchen','bathroom','hallway']
    random_choice=random.choice(rooms)
    if random_choice=='bedroom':
        bedroom()
    if random_choice=='kitchen':
        kitchen()
    if random_choice=='bathroom':
        bathroom()
    if random_choice=='hallway':
        hallway()
    

def bedroom():
    print('You are in the bedroom. Where do you want to go? ')
    print('1- bathroom')
    print('2- hallway')
    n=int(input('Where do you want to go: '))
    if n==1:
        bathroom()
    if n==2:
        hallway()

def kitchen():
    print('You are in the kitchen. Where do you want to go? ')
    print('1- hallway')
    print('2- window')
    n=int(input('Where do you want to go?'))
    if n==1:
        hallway()
    if n==2:
        print('You died')
        

def bathroom():
    print('You are in the bathroom. Where do you want to go? ')
    print('1- hallway')
    print('2- bedroom')
    n=int(input('Where do you want to go? '))
    if n==1:
        hallway()
    if n==2:
        bedroom()
    
    

def hallway():
    print('You are in the hallway. Where do you want to go?')
    print('1- bedroom')
    print('2- bathroom')
    print('3- kitchen')
    print('4- door')
    n=int(input('Where do you want to go? '))
    if n==1:
        bedroom()
    if n==2:
        bathroom()
    if n==3:
        kitchen()
    if n==4:
        print('1-Yes')
        print('2-No')
        x=int(input('You won!! \nWant to play again?'))
        if x==1:
            main_menu()
        else:
            print('END')
    
main_menu()


