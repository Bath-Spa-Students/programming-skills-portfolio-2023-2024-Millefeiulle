#Write a loop that allows the insert of a series of pizza toppings until a 'quit' value is entered, as each topping is added.
#print the message about the topping on their pizza.

prompt = "\nWhat topping do you want on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I will add {topping} to your pizza.")
    else:
        break