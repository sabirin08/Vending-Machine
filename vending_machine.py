"""

Program Description:
This program implements an object of the VendingMachine class and allows the user to enter multiple commands (buy, check inventory, restock) as input until a stop word is detected.

Author: Sabirin Mohamed
"""
class VendingMachine:
    def __init__(self, soda_count, coffee_count, water_count):
        self.soda_count = soda_count
        self.coffee_count = coffee_count
        self.water_count = water_count

    def purchase(self, drink_type):
        if drink_type == 1:
            if self.soda_count > 0:
                self.soda_count -= 1
            else:
                print("Soda is out of stock.")
        elif drink_type == 2:
            if self.coffee_count > 0:
                self.coffee_count -= 1
            else:
                print("Coffee is out of stock.")
        elif drink_type == 3:
            if self.water_count > 0:
                self.water_count -= 1
            else:
                print("Water is out of stock.")
        else:
            print("Invalid drink type. Please select a valid option.")

    def restock(self, drink_type, amount):
        if drink_type == 1:
            self.soda_count += amount
        elif drink_type == 2:
            self.coffee_count += amount
        elif drink_type == 3:
            self.water_count += amount
        else:
            print("Invalid drink type. Please select a valid option.")

    def report_inventory(self):
        print("Inventory")
        print(f"Soda: {self.soda_count} bottles")
        print(f"Coffee: {self.coffee_count} bottles")
        print(f"Water: {self.water_count} bottles")


vending_machine = VendingMachine(10, 10, 10)

while True:
    instruction = input("Would you like to buy, check inventory, or restock?: ").lower()

    if instruction in ['quit', 'q']:
        vending_machine.report_inventory()
    elif instruction == 'buy':
        print("Please select an option:")
        print("1 - Soda\n2 - Coffee\n3 - Water")
        drink_type = int(input(":> "))
        vending_machine.purchase(drink_type)
    elif instruction == 'restock':
        print("Please select an option:")
        print("1 - Soda\n2 - Coffee\n3 - Water")
        drink_type = int(input(":> "))
        amount = int(input("Please enter an amount:\n:> "))
        vending_machine.restock(drink_type, amount)
    elif instruction == 'check inventory':
        vending_machine.report_inventory()
    else:
        print("Invalid. Please enter a valid instruction.")
