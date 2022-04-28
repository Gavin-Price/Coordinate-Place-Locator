x = int(input('Enter X-axis value:'))

y = int(input('Enter Y-axis value:'))

if x > 0 and y > 0: 
    print(' Quadrant 1')

elif x < 0 and y > 0:
    print(' Quadrant 2')
    
elif x < 0 and y < 0:
    print (' Quadrant 3')
    
elif x > 0 and y < 0: 
    print (' Quadrant 4')

elif x == 0 and y > 0: 
    print(' Y axis') 
    
elif x == 0 and y < 0: 
    print( ' Y axis')
    
elif x < 0 and y == 0: 
    print(' X axis')
    
elif x > 0 and y == 0:
    print(' X axis')
    
else:
    print(' Origin')
    
    

    