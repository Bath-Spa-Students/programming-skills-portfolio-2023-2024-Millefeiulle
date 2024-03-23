#If the alien color is green, print a message that the player earned 5 points.
#If the alien is yellow, print a message that the player earned 10 points.
#If the alien is red, print a message that the player earned 15 points.
#Write three versions of this program, ensuring each message is printed for the appropriate color alien.
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

alien_color = 'yellow'

if alien_color == 'green':
	print("You just earned 5 points.")
elif alien_color =='yellow':
	print("You just earned 10 points.")
else: 
	print("You just earned 15 points.")

alien_color = 'green'

if alien_color == 'green':
	print("You just earned 5 points.")
elif alien_color == 'yellow':
	print("You just earned 10 points.")
else: 
	print("You just earned 15 points.")	
