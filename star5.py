"""r=int(input())        #reverse triangle
for i in range(r):      
    for j in range(i):
        print(" ",end="")
    for k in range(2*r-1-2*i):
         print("*",end="")
    print()"""
    
    
    
r=int(input())
for i in range(r):         #for i in range(r-1,-1,-1) for reverse triangle
    for j in range(r-i):
        print(" ",end="")
    for k in range(2*i+1):
         print("*",end="")
    print()