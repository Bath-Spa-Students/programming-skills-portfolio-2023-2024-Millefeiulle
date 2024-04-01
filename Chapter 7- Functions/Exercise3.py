#Write a function called make_shirt() that accepts a size and the message that gets printed on the shirt.
#print a sentence summarizing the size of the shirt and the message printed on it.
def make_shirt(size, message):
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt('medium', 'Coding is fun!')
make_shirt(message="Stay positive", size='large')