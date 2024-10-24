n=input()
ans=""
for i in n:
    if i==".":
        ans=ans+"[.]"
    else:
        ans=ans+i
print(ans)