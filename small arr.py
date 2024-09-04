n1 = list(map(int, input().split()))
if len(n1) <= 3:
    print(0)
else:
    even= n1[0::2]
    odd= n1[1::2]
    if len(even) > 1:
        even.sort()
        largest_even = even[-2]  
    else:
        largest_even= 0  
    if len(odd) > 1:
        odd.sort()
        largest_odd= odd[-2]  
    else:
        largest_odd = 0 
    print(largest_even +largest_odd)
    
