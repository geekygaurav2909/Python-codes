# Write your code below this line 👇

def prime_checker(number):
    is_prime = False
    for i in range(2, number):
        if number % i == 0:
            is_prime = True
    
    if is_prime:
        print("The Number is not a prime")
    else:
        print("The number is a prime")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
