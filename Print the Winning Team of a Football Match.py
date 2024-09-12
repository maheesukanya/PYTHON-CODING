n=int(input())
a1=input()
a2=int(input())
b1=input()
b2=int(input())
c1=input()
c2=int(input())
if a2 >= b2 and a2 >= c2:
    max_goals = a2
    team = a1
elif b2 >= a2 and b2 >= c2:
    max_goals = b2
    team = b1
else:
    max_goals = c2
    team = c1
print(team+" "+str(max_goals))