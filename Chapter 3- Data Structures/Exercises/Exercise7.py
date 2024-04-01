#Store the locations in a list. Make sure the list is not in alphabetical order.
locations = ['Tokyo', 'Paris', 'Bangkok', 'Lima', 'Rome']

#Print your list in its original order.
print("Original order:")
print(locations)

#Use sorted() to print your list in alphabetical order without modifying the actual list.
print("\nAlphabetical:")
print(sorted(locations))

#Show that your list is still in its original order by printing it.
print("\nOriginal order:")
print(locations)

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

#Show that your list is still in its original order by printing it again.
print("\nOriginal order:")
print(locations)

#Use reverse() to change the order of your list. Print the list to show that its order has changed.
print("\nReversed:")
locations.reverse()
print(locations)

#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
print("\nOriginal order:")
locations.reverse()
print(locations)

#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
print("\nAlphabetical")
locations.sort()
print(locations)

#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)