
rivers = {
    'Amazon': 'Brazil',
    'Yangtze': 'China',
    'Yenisei': 'Russia',
    }

#print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

#print the name of each river included in the dictionary.
#print the name of each country included in the dictionary.
print()
[print(river) for river in rivers.keys()]
print()
[print(country) for country in set(rivers.values())]