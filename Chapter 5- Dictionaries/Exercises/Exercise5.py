# create an empty list to store the pets in.
pets = []

# create different pets and store each one in the list.
pet = {
    'animal type': 'cat',
    'name': 'luna',
    'owner': 'michael',
    'weight': 4,
    'diet': 'fish',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'Cookie',
    'owner': 'jessie',
    'weight': 38,
    'diet': 'meat',
}
pets.append(pet)

pet = {
    'animal type': 'horse',
    'name': 'bella',
    'owner': 'annie',
    'weight': 90,
    'diet': 'corn',
}
pets.append(pet)

# Showcase information about each pet.
for pet in pets:
    print(f"\nThis is what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")