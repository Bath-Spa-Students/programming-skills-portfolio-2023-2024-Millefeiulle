#Add a prompt which asks for age.
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are done. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

#If a person is under the age of 3, the ticket is free.
#if they are between 3 and 12, the ticket is $10
#if they are over age 12, the ticket is $15
#print the message accordingly.

    if age < 3:
        print("You get in for free!")
    elif age < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")