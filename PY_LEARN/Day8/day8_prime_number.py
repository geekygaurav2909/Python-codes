# Write your code below this line 👇

prime_list = [2,3,5,7]

def prime_checker(number):
    counter = []
    for num in range(len(prime_list)):
        mod = number % prime_list[num]
        counter.append(mod)

    if 0 in counter:
        print("The number is not a prime")
    else:
        print("This is a prime number")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)