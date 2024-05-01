print("Hello, Welcome to the Tip Calculator Program! \n\n")

#Total bill
bill_amount = float(input("What was the total bill $ "))

#Input the desired tip percentage
desired_tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))

#Input the bill split among the number of people
bill_split = int(input("How many people to split the bill? "))

net_bill_split = ((bill_amount * desired_tip_percent) / 100 +  bill_amount)
net_bill_split /= bill_split

final_bill = round(net_bill_split,2)

billShare = "{:0.2f}".format(final_bill)

print(f"Each Person Should pay: {billShare}")
