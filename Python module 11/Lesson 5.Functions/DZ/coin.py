def coin(x,y):
    if x<=1.0 and y<=1.0 and x>=-1.0 and y>=-1.0:
        print('The coin is somewhere near')
    else:
        print('The coin is not in the area')
x=float(input('Insert the coordinate x: '))
y=float(input('Insert the coordinate y: '))
coin(x,y)
