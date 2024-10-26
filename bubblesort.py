#BUBBLE SORT
n=list(map(int,input().split()))
for i in range(0,len(n)-1):
    for j in range(0,len(n)-i-1):
        if(n[j]>n[j+1]):                #if(n[j]<n[j+1]):   (for descending order)                    
            n[j],n[j+1]=n[j+1],n[j]
print(n)


#general sorting method
"""a=[4,6,2,3,9,5]
a.sort()       #for descending order a.sort(reverse=True)
print(a)"""

"""a=[4,6,2,3,9,5]
b=sorted(a)        #b=sorted(a,reverse=True)  for descending order
print(b)"""




    