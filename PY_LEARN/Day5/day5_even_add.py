target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
totalSum = 0

for counter in range(0, target+1,2):
  totalSum +=counter
  
print(totalSum)
