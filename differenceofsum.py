a=int(input())
b=int(input())
sum_not=0
sum=0
for i in range(1,a+1):
    if i%b!=0:
        sum_not=sum_not+i
    else:
        sum=sum+i
print(sum_not-sum)
        
        
      
        