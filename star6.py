"""r=int(input())
for i in range(r-1):         
    for j in range(r-i):
        print(" ",end="")
    for k in range(2*i+1):
         print("*",end="")
    print()
for i in range(r-1,-1,-1):        
    for j in range(r-i):
        print(" ",end="")
    for k in range(2*i+1):
         print("*",end="")
    print()"""
    
    
r=int(input())
for i in range(r-1,-1,-1):        
    for j in range(r-i):
        print(" ",end="")
    for k in range(2*i+1):
         print("*",end="")
    print()
for i in range(1,r):         
    for j in range(r-i):
        print(" ",end="")
    for k in range(2*i+1):
         print("*",end="")
    print()