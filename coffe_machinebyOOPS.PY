from menu import Menu,MenuItem
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine=MoneyMachine()
Coffee_maker=CoffeeMaker()
# my_money_machine.report()
# Coffee_maker.report()
drink=Menu()
coffee=True
while coffee:
    options=drink.get_items()
    choice=input(f"What would u like to have?{options}")
    if choice=="report":
       my_money_machine.report()
       Coffee_maker.report()
    elif choice=="off":  
        coffee=False
    else:
       prefer= drink.find_drink(choice)
       if Coffee_maker.is_resource_sufficient(prefer):
            if my_money_machine.make_payment(prefer.cost):
                Coffee_maker.make_coffee(prefer)
        

        
        

   
