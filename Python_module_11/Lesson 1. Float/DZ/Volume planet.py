
earth=10.8321*10**11
r=float(input('Insert the radius of your planet: '))
volume=4/3*3.14*r**3
if volume>earth:
    print('The earth is smaller than your planet by: ',round(volume/earth,3))
if earth>volume:
    print('The earth is bigger than your planet by: ',round(earth/volume,3))

