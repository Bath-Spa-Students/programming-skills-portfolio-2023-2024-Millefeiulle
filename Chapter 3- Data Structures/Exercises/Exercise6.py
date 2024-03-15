# Invite a few people to dinner.
guests = ['Jack','Tim','lynda']

# print the invitation message for guests
name = guests[0].title()
print("Hi " + name +", I would like to invite you to dinner.")

name = guests[1].title()
print("Hi " + name +", I would like to invite you to dinner.")

name = guests[2].title()
print("Hi " + name +", I would like to invite you to dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

# Tim can't make it so i'll invite Alison instead.
del(guests[1])
guests.insert(1, 'Alison')

# Print the invitations again.
name = guests[0].title()
print("\n" +"Hi " + name +", I would like to invite you to dinner.")

name = guests[1].title()
print("Hi " + name +", I would like to invite you to dinner.")

name = guests[2].title()
print("Hi " + name +", I would like to invite you to dinner.")

# Unfortunately, the table won't arrive on time.
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

# There should be two people left to be invited.
name = guests[0].title()
print("Hi " + name +", I would like to invite you to dinner.")

name = guests[1].title()
print("Hi " + name +", I would like to invite you to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)