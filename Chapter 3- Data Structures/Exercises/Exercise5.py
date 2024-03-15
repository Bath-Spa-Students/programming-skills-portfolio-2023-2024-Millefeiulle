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