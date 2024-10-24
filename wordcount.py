"""a = input().split(",")
ans=0
for i in range(len(a)):  
    count=1
    for j in a[i]:
        if j == " ":  
            count += 1 
    ans=max(ans,count)
print(ans)"""       #this code counts the leading and trailing spaces 
         
         

a = input().split(",")  # Splitting the input by commas
ans = 0  # To store the maximum word count

for i in range(len(a)):  
    # Strip leading and trailing spaces, then count words by splitting on spaces
    b= a[i].strip()  
    count = len(b.split())  # Count words by splitting the stripped sentence by spaces
    ans = max(ans, count)  # Update the maximum word count

print(ans)  # Print the maximum word count found"""

