n=list(map(int,input().split()))
m=0
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]!=n[j]:
            a=abs(j-i)
            m=max(m,a)
print(m)
            
        
