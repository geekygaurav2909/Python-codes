#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

selected_letter =random.sample(letters,nr_letters)
resulted_letter = ''.join(map(str,selected_letter))

selected_number = random.sample(numbers,nr_numbers)
resulted_number = ''.join(map(str,selected_number))

selected_symbol = random.sample(symbols,nr_symbols)
resulted_symbol = ''.join(map(str, selected_symbol))

final_password = resulted_letter + resulted_number + resulted_symbol
password_list = list(final_password)


random.shuffle(password_list)
shuffled_password = ''.join(password_list)

print(f"The final password is {final_password} and shuffedld is {shuffled_password}")

# contact = ''.join([str(value) for value in selected_symbol])
# print(resulted_symbol)

# counter = 0
# for symbols_cat in symbols:
#     sym_rand = random.randint(0,len(symbols)-1)
#     for value_sys in symbols[sym_rand]:
#         counter += value_sys
#         print(f"here is the value_sys: {value_sys} and counter_val is{counter}")
#     # value_sys = symbols[sym_rand]
#     # print(f"{sym_rand} and value at {value_sys} ")

    



# print(f"The random number is :{alpharand}")
# valueAlpha = symbols[alpharand]
# print(f"The value at random numbre number is: {valueAlpha} and {len(symbols)}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P