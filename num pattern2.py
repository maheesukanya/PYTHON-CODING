n=int(input())
for i in range(n):
    for j in range(n-1-i):
        print(" ",end=" ")
    for k in range(i+1,0,-1):
        print(k,end=" ")
    print()