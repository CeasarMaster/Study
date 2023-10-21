fsize=int(input('Insert the file size: '))
ispeed=int(input('Insert the speed of your connection: '))
counter=1

for i in range(ispeed,fsize+1,ispeed):
    percent4=(i)/(fsize/100)
    print(counter,'sec. passed.','Downloaded',i,'out of',fsize,'('+str(int(percent4))+'%'+')')
    counter+=1
if fsize%ispeed!=0:
    print(counter,'sec. passed.','Downloaded',fsize,'out of',fsize,'('+'100'+'%'+')')
    
   
    
   
        
       
        

