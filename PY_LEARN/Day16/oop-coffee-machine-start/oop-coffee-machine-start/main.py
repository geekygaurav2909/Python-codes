from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

profit = 0
prepare_coffee = CoffeeMaker()
menu = Menu()
money_calc = MoneyMachine()
should_continue = True

while should_continue:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ").lower()
    if user_input == 'off':
        should_continue = False
    elif user_input == 'report':
        prepare_coffee.report()
        money_calc.report()
    else:
        drink = menu.find_drink(user_input)
        resource_validation = prepare_coffee.is_resource_sufficient(drink)

        if resource_validation:
            order_accepted = money_calc.make_payment(drink.cost)

            if order_accepted:
               prepare_coffee.make_coffee(drink)
        else:
            print(resource_validation)
            if(input("Would you like to add the resources: Type 'y' if you are admin. Otherwise 'n'.: ").lower()) == 'y':
                prepare_coffee.add_resources()
                print("****** Here is the final resources available after refill *******")
                prepare_coffee.report()
                money_calc.report()
            else:
                print("Sorry, You don't have permissison to add the resources.")
            