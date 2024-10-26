n=input().split()
dic={}
for i in range(len(n)):
    k=n[i]
    if k not in dic:
        dic[k]=1
    else:
        dic[k]+=1
for j in dic:
    print(j,"->",dic[j])