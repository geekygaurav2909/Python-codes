print("Welcome to the Leap year finder!")

year = int(input("Please enter the year. ex: 2004, 2400 "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
      print("Leap year")
else:
    print("Not a leap year")