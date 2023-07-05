from menu import MENU
from resources import resources

def calculate_money_inserted():
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

def reduce_water(type_coffee):
    reduced_water = resources["water"] - MENU[type_coffee]["ingredients"]["water"]
    return reduced_water

def reduce_milk(type_coffee):
    reduced_milk = resources["milk"] - MENU[type_coffee]["ingredients"]["milk"]
    return reduced_milk

def reduce_coffee(type_coffee):
    reduced_coffee = resources["coffee"] - MENU[type_coffee]["ingredients"]["coffee"]
    return reduced_coffee

def add_money():
    money_inside = resources["money"] + calculate_money_inserted()
    return money_inside

def calculate_change(type_coffee):
    return round(calculate_money_inserted() - MENU[type_coffee]['cost'],2)

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

another_customer = True
while another_customer:
    question = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if question == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    elif question == 'off':
        another_customer = False
    else:
        if is_resource_sufficient(MENU[question]['ingredients']):
            print("Please insert coins.")
            quarters = int(input("how many quarters? "))
            dimes = int(input("how many dimes? "))
            nickles = int(input("how many nickles? "))
            pennies = int(input("how many pennies? "))
            if calculate_money_inserted() >= MENU[question]["cost"]:
                resources["coffee"] = reduce_coffee(question)
                resources["milk"] = reduce_milk(question)
                resources["water"] = reduce_water(question)
                resources["money"] = add_money() - calculate_change(question)
                print(f"Here is ${calculate_change(question)} in change.")
                print(f"Here is your {question}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
