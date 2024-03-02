# Import the 'datetime' module to work with date and time
import datetime

# Acquire the current date and time
now = datetime.datetime.now()

# Create a datetime object showing the current date and time

# Show a memo showing what is being printed
print("Current date and time : ")

# Print the current date and time in a specified format
print(now.strftime("%Y-%m-%d %H:%M:%S"))