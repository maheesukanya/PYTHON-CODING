n=int(input())
m=bin(n)[2:]
sum=0
for i in m:
    sum=sum+int(i)
print(sum)