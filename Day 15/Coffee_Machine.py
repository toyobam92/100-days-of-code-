
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']

machine_on = True
while machine_on:
    user_choice = input("What would you like?(espresso,latte,cappuccino):")
    if user_choice == "latte" or user_choice == "cappuccino":
        user_water = MENU[user_choice]['ingredients']['water']
        user_milk = MENU[user_choice]['ingredients']['milk']
        user_coffee = MENU[user_choice]['ingredients']['coffee']
        if water < user_water:
            print('Sorry there is not enough water')
        elif coffee < user_coffee:
            print('Sorry there is not enough coffee')
        elif milk < user_milk:
            print('Sorry there is not enough milk')
        else:
            print("Please insert coins")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total_bill = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
            cost = MENU[user_choice]['cost']

            if total_bill < cost:
                print("Sorry that's not enough. Money refunded.")

            elif total_bill >= cost:
                print(f"Here is ${round(total_bill - cost, 3)} in change")
                print(f"Here is your {user_choice} Enjoy!")

                money += cost
                water -= user_water
                coffee -= user_coffee
                print(coffee)

    elif user_choice == "espresso":
        user_water = MENU[user_choice]['ingredients']['water']
        user_coffee = MENU[user_choice]['ingredients']['coffee']

        if water < user_water:
            print('Sorry there is not enough water')
        elif coffee < user_coffee:
            print('Sorry there is not enough coffee')
        else:
            print("Please insert coins")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total_bill = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
            cost = MENU[user_choice]['cost']

            if total_bill < cost:
                print("Sorry that's not enough. Money refunded.")

            elif total_bill >= cost:
                print(f"Here is ${round(total_bill - cost, 3)} in change")
                print(f"Here is your {user_choice} Enjoy!")

                money += cost
                water -= user_water
                coffee -= user_coffee
                print(coffee)

    elif user_choice == "off":
        machine_on = False
        break
    elif user_choice == "report":
        print(f"Water {water}ml")
        print(f"Milk {milk}ml")
        print(f"Coffee {coffee}g")
        print(f"Money ${money}")

