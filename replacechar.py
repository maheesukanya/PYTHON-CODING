n=input()
ch1=input()
ch2=input()
result=[]
for i in range(len(n)):
    if n[i]==ch1:
        result.append(ch2)
    elif n[i]==ch2:
        result.append(ch1)
    else:
        result.append(n[i])
print(''.join(result))
        
        