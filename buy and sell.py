"""price=list(map(int,input().split()))
n=len(price)
ans=0
for i in range(n):
    for j in range(i+1,n):
        temp=price[j]-price[i]
        ans=max(ans,temp)
print(ans)"""
            
            
"""price=list(map(int,input().split()))
minval=price[0]
ans=0
for i in range(1,len(price)):
    ans=max(ans,(price[i]-minval))
    minval=min(minval,price[i])
print(ans)"""


p=list(map(int,input().split()))
a=min(p)
b=max(p)
print(abs(a-b))
    