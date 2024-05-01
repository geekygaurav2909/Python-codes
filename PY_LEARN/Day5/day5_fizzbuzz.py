number_data = 0
for counter in range(1, 101, 1):
    number_data = counter
    if number_data % 3 == 0 and number_data % 5 == 0:
        print("FizzBuzz")
        print(counter.__index__())
    elif number_data % 3 == 0:
        print("Fizz")
    elif number_data % 5 == 0:
        print("Buzz")
    else:
        print(counter)
    