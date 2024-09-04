n = input()
if len(n) == 0:
    print(-1) 
else:
    a = int(n[0]) 
    for i in range(1, len(n) - 1, 2):  
        if n[i] == 'A':
            a = a & int(n[i + 1])
        elif n[i] == 'B':
            a = a | int(n[i + 1])
        else:
            a = a ^ int(n[i + 1])
    print(a) 
    
        