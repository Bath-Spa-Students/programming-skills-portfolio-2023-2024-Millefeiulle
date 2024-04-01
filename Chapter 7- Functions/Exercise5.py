#Write a function called describe_city() that accepts the name of a city and its country.
#print the statement about the countries, one country not being the default.
def describe_city(city, country='Japan'):
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Kyoto')
describe_city('Dhaka', 'Bangladesh')
describe_city('Osaka')