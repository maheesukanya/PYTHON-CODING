arr=list(map(int,input().split()))
arr.reverse()
a=[]
b=[]
for i in range(len(arr)):
    if(i%2==0):
        a.append(arr[i])
    else:
        b.append(arr[i])
print(" ".join(map(str, a)))
print(" ".join(map(str, b)))