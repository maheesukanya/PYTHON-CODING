n = int(input())
magical_count = 0
for i in range(1, n + 1):
    a = bin(i)[2:]  # Convert the number to binary and remove the '0b' prefix
    b = a.replace("10", "1")
    b = b.replace("1", "2")
    sum_digits = 0
    for j in b:
        sum_digits += int(j)  
    if sum_digits % 2 == 1:  
        magical_count += 1
print(magical_count)
