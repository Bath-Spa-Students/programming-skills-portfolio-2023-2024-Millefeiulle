#List of the names of various sandwiches.
sandwich_orders = ['chicken', 'grilled cheese', 'egg', 'turkey']
finished_sandwiches = []

#Loop through the list of sandwich orders and print a message for each order.
while sandwich_orders:
    unfinished_sandwich = sandwich_orders.pop()
    print(f"I'm making your {unfinished_sandwich} sandwich.")
    finished_sandwiches.append(unfinished_sandwich)

#print a message listing each sandwich that was made.
print("\n")
for sandwich in finished_sandwiches:
    print(f"I have made a {sandwich} sandwich.")