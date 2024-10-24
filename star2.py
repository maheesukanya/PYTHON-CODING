n=int(input())
for i in range(n):
    for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
    

"""r=int(input())
c=int(input())
for i in range(r):
    for j in range(c):
            if i==0 or i==r-1 or j==0 or j==c-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()"""