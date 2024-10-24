"""n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        if k==0 or k==i*2 or i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()"""
    
    
n=int(input())
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        if k==0 or k==i*2 or i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()