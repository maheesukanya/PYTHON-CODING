from itertools import permutations
n=input()
v=[]
for i in n:
    if i in 'aeiou':
        v.append(i)
b=list(permutations(v))
print(b)