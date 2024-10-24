li = input().split()
x = 0
for i in range(len(li)):
    if li[i] == "X--" or li[i] == "--X":
        x -= 1
    else:
        x += 1
print(x)
