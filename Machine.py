class VendingMachine:
    def __init__(self):
        # Sets the vending machine with a menu, stock and money variables.
        self.menu = {
            "1": {"item": "Bottled Water", "price": 0.75, "stock": 8},
            "2": {"item": "Lipton Green Tea", "price": 1.15, "stock": 5},
            "3": {"item": "Frappuccino Coffee Drink", "price": 2.50, "stock": 9},
            "4": {"item": "Lipton Peach Tea", "price": 1.15, "stock": 7},
            "5": {"item": "Diet Pepsi", "price": 1.00, "stock": 4},
            "6": {"item": "Nacho Cheese", "price": 1.45, "stock": 6},
            "7": {"item": "Pringles", "price": 1.00, "stock": 5},
            "8": {"item": "Mars Chocolate Bar", "price": 1.50, "stock": 7},
            "9": {"item": "Nature Valleys Protein Bar", "price": 1.65, "stock": 6},
            "10": {"item": "Twix Chocolate Bar", "price": 1.50, "stock": 8}
        }   
        self.inserted_amount = 0.00
        self.total_balance = 0.00
    
    def display_heading(self):
        # Present a welcoming message.
        print("""Welcome to Vendigo's Vending Machine""")

    def display_menu(self):
        # Show the items from the menu beside their prices and stock status.
        print("\nMENU:")
        for code, item in self.menu.items():
            stock_status = "" if item["stock"] > 0 else "(Sold Out)"
            print(f"{code}:  {item['item']} - ${item['price']:.2f} {stock_status}")

    def money_input(self):
        # Remind the customer to insert cash and deal with illogical inputs.
        while True:
            try:
                self.inserted_amount += float(input("Insert cash: "))
                break
            except ValueError:
                print("Invalid input. Please enter the correct amount.")

    def code_input(self):
        # Remind the customer to enter the code of the item they wish to purchase.
        while True:
            code = input("Enter the code of the item you wish to purchase (Type 'no' to stop): ").upper()
            if code == 'NO':
                return code
            if code in self.menu and self.menu[code]["stock"] > 0:
                return code
            elif code in self.menu and self.menu[code]["stock"] == 0:
                print("Unfortunately, this is sold out. Please make another selection.")
            else:
                print("Invalid code. Please enter the correct code.")

    def item_dispense(self, item):
        # Show a message stating that the item is being dispensed.
        print(f"\nDispensing {item}...")

    def evaluate_balance(self, inserted_amount, item_price):
        # Evaluate and return the balance after the purchase.
        return inserted_amount - item_price
    
    def item_suggestion(self, item):
        # Supply a suggestion depending on the purchased item.
        suggestions = {
            'Lipton Green Tea': 'Give Nature Valleys Protein Bar a try with it.',
            'Frappuccino Coffee Drink': 'How about adding a snack like Twix Chocolate Bar?',
            'Nature Valleys Protein Bar': 'Consider pairing it with Lipton Green Tea.',
            'Twix Chocolate Bar': 'Why not get a energizing cup of Frappuccino Coffee Drink to go along with it.'
        }
        return suggestions.get(item, '')
    
    def run(self):
        #This runs the vending machine.
        self.display_heading()
        self.display_menu()
        self.money_input()
        initial_cash = self.inserted_amount
        continue_purchase = True
        while continue_purchase:
            code = self.code_input()
            if code == 'NO':
                break
            item = self.menu[code]
            price = item["price"]
            if self.inserted_amount < price:
                print("Insufficient amount.")
                customer_input = input("Do you wish to insert more cash? (Type 'yes' or 'no'): ").upper()
                if  customer_input == 'YES':
                    self.money_input()
                    continue
                else:
                    break
            balance = self.evaluate_balance(self.inserted_amount, price)
            self.item_dispense(item["item"])
            self.total_balance += balance
            suggestion = self.item_suggestion(item["item"])
            if suggestion:
                print(suggestion)
            item["stock"] -= 1
            if all(item["stock"] == 0 for item in self.menu.values()):
                print("Unfortunately, the vending machine is currently out of stock.")
                break
            self.inserted_amount = balance
            # Inquire the customer if they wish to continue to make another purchase.
            customer_input = input("Do you wish to continue your purchase? (Type 'yes' to continue or 'no' to quit): ").upper()
            continue_purchase = customer_input == 'YES'
        remainder_cash = self.inserted_amount
        self.inserted_amount = initial_cash
        print(f"Total balance: ${remainder_cash:.2f}")
        print("\nThank you for using Vendigo's Vending Machine!")

#This enables to run the vending machine overall.
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()



