MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },

    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
         "cost":3.0,
    }
}

profit=0
coffee_machine={
    "water":300,
     "milk":200,
     "coffee":100,
     "money":profit
}
def sufficient(resources):
    is_enough=True
    for i in resources:
        if resources[i]>=coffee_machine[i]:
            print("sorry there is not enough {i}")
            is_enough=False
    return is_enough

def make_coffee(drinkname,resources):
        for i in resources:
            coffee_machine[i]-=resources[i]
        print(f"ur drinkname:{drinkname}")

                
def coins():
    print("please enter coins")
    total=int(input("how many quarters?"))*0.25
    total+=int(input("how many dimes?"))*0.1
    total+=int(input("how many nickels?"))*0.05
    total+=int(input("how many pennies?"))*0.01
    return total

def transaction(money_recieved,drink_cost):
    if money_recieved>=drink_cost:
        change=round(money_recieved-drink_cost,2)#upto two decimal faces 
        print(f"change is:Rs{change}")
        global profit
        profit+=drink_cost##as here profit is act as local sccope and sabove it is in global scope so gloabal keyword use to use profit here
        return True
    else:
        print("not enough money.money refund")
        return False

coffee=True
while coffee:
    choice=input("What would u like to have?(espresso/latte/cappuccino) or report,or off").lower()
    if choice=="report":
        print(coffee_machine )
    elif choice=="off":  
        coffee=False
    else:
        drink=MENU[choice]
        if sufficient(drink["ingredients"]):
            payment=coins()
            if transaction(payment,drink["cost"]):
                make_coffee(drinkname=choice,resources=drink["ingredients"])


             

    
            