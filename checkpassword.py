n = input("Enter a string: ")   
a = len(n)
if a < 4:  
    print(0)
else:  
    if n[0].isdigit():  
        print(0)
    else:
        cap = 0
        num = 0
        for i in range(a):  
            if n[i] == ' ' or n[i] == '/': 
                print(0)
                break  
            if n[i].isupper():  
                cap += 1
            elif n[i].isdigit():  
                num += 1
        if cap > 0 and num > 0:  
            print(1)
        else:
            print(0)
