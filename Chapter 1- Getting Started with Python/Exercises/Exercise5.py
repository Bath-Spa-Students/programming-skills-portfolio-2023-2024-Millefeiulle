# Import the 'pi' constant from the 'math' module
from math import pi

# Prompt the user to input the radius of the circle 
r = float(input("Input the radius of the circle : "))

# Calculate the area of the circle using the formula: area = π * r^2
area = pi * r ** 2

# Show the result, including the radius and calculated area
print(" The area of the circle with radius " + str(r) + " is: " + str(area))
