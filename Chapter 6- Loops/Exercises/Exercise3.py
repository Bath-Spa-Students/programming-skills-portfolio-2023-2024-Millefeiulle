#Write a loop that never ends since there no 'quit' value.
prompt = "How old are you?"

while True:
    age = input(prompt)
    
    age = int(age)
    if age < 3:
        print("You get in for free!")
    elif age < 12:
        print("Your ticket is $10") 
    else:
        print("Your ticket is $15")