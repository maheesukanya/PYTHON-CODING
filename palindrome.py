a=input()
n=len(a)
i=0
j=n-1
while(i<j):
    if(a[i]!=a[j]):
        print("not palindrome")
        break
    i+=1
    j-=1
    
else:
    print("palindrome")