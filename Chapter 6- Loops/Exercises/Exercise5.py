#The list of the names of various sandwiches.
#The sandwich 'pastrami' appears in the list at least three times.
sandwich_orders = [
    'pastrami', 'chicken', 'grilled cheese', 'pastrami',
    'pastrami', 'egg', 'turkey', 'pastrami']
finished_sandwiches = []

#print a message saying the deli has run out of pastrami and then use a loop to remove any pastrami sandwich order from sandwich_orders.
print("Unfortunately, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#loop through the list of sandwich orders and print a message for each order.
print("\n")
while sandwich_orders:
    unfinished_sandwich = sandwich_orders.pop()
    print(f"I'm making your {unfinished_sandwich} sandwich.")
    finished_sandwiches.append(unfinished_sandwich)

#print a message listing each sandwich that was made.
print("\n")
for sandwich in finished_sandwiches:
    print(f"I have made a {sandwich} sandwich.")
