
# To generate squares of numbers

def squares(n):
    print('Genearted squares from 1 to {0}'.format(n**2))
    for i in range(1,n+1):
        yield i**2


while(1):
    m=int(input("Enter choice 1. Continue or 0. Exit \n"))
    if(m==1):
        n = int(input("Enter value for n : \n"))
        gen = squares(n)

        for x in gen:
            print(x, end = ' ')
       
    elif(m==0):
        break
        
        
    
    
    
    
    