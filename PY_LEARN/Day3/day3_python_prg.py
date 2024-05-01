print("Hey! Welcome to Rollercoaster!")

#Enter the height
height = int(input("Enter your height in CM please: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What your age?"))
    if age < 12:
        bill = 5
        print("Child ticket price is $5.")
    elif age <=18:
        bill = 7
        print("Youth Ticket price is $7.")
    elif age <=22:
        bill = 10
        print("Adult Ticket Price is $10.")
    else:
        bill = 12
        print("You need to pay $12.")

    wantsPhotos = str(input("Do you want photos, press Y or N: "))

    if wantsPhotos == "Y":
        bill += 3
    print(f"Your total bill including the photos is ${bill}") 
else:
    print("Sorry, you have grow taller for the rollercoaster ride!")