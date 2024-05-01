from day15_coffee_data import MENU, resources

def fetch_check_resources(drink):
    """Takes item name as input and returns the resource availability."""
    #Once again, For loop helped me to avoid multiple conditional checks.
    for item in MENU[drink]["ingredients"]:
        if report[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry, There isn't enought {item}")
            return False
    return True

    # water = MENU[drink]["ingredients"]["water"]
    # if drink != 'espresso':
    #     milk = MENU[drink]["ingredients"]["milk"]
    # coffee = MENU[drink]["ingredients"]["coffee"]
    # available = False

    # if water > report["water"]:
    #     return "Sorry, There isn't enough water."
    # elif drink != 'espresso':
    #     if milk > report["milk"]:
    #         return "Sorry, There isn't enough milk."
    # elif coffee > report["coffee"]:
    #     return "Sorry, There isn't enough coffee."
    # else:
    #     return available == True


def currency_inserted(drink):
    """Performs the currency conversion and returns the final change as output. If coin is less then returns false."""
    print("  Please insert coins. \n")
    quaters = int(input("   How many quaters?: "))
    dimes = int(input("   How many dimes?: "))
    nickles = int(input("   How many nickles?: "))
    pennies = int(input("   How many pennies?: "))

    total_received = quaters*.25 + dimes*.10 + nickles*.05 + pennies*.01
    drink_cost = MENU[drink]["cost"]

    if total_received < drink_cost:
        return False
    else:
        return total_received - drink_cost


def resource_update(input_drink):
    print(f"Before update: {report}")
    # report["water"] -= MENU[input_drink]["ingredients"]["water"]
    # if input_drink != 'espresso':
    #     report["milk"] -= MENU[input_drink]["ingredients"]["milk"]
    # report["coffee"] -= MENU[input_drink]["ingredients"]["coffee"]
    # report["money"] += MENU[input_drink]["cost"]

    #Learning: Used for loop this way, we don't have to write update for every items.
    for item in MENU[input_drink]["ingredients"]:
        report[item] -= MENU[input_drink]["ingredients"][item]
    report["money"] += MENU[input_drink]["cost"]
    print(f"After update: {report}")

report = {}
should_continue = True

report = resources
report["money"] = 0

while should_continue:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'off':
        should_continue = False
    elif user_input == 'report':
        print(f"Water: {report['water']}ml\nMilk: {report['milk']}ml\nCoffee: {report['coffee']}g\nMoney: ${report['money']}")
    else:
        resource_validation = fetch_check_resources(user_input)

        if resource_validation:
            change_returned = currency_inserted(user_input)
            if not change_returned:
                print("Sorry, that's not enough money. Money refunded")
            else:
                change_returned = round(change_returned,2)
                resource_update(user_input)
                print(f"Here is ${change_returned} in change.")
                print(f"Here is your {user_input} Enjoy!")
        else:
            print(resource_validation)
            if(input("Would you like to add the resources: Type 'y' if you are admin. Otherwise 'n'.: ").lower()) == 'y':
                report["water"] += int(input("Enter the water quantity: "))
                report["milk"] += int(input("Enter the milk quantity: "))
                report["coffee"] += int(input("Enter the coffee quantity: "))
                print("****** Here is the final resources available after refill *******")
                print(f"Water: {report['water']}ml\nMilk: {report['milk']}ml\nCoffee: {report['coffee']}g\nMoney: ${report['money']}")
            else:
                print("Sorry, You don't have permissison to add the resources.")
            