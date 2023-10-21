def monetka(a,b,c):
    hyp=(x**2+y**2)**(1/2)
    if hyp<=r:
        print('The coin is somewhere near')
    else:
        print('The coin is not in the area')




x=float(input('Insert coordinate x: '))
y=float(input('Insert coordinate y: '))
r=float(input('Insert the radius: '))

monetka(x,y,r)



