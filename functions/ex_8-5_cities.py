# write a function called describe_city() that accepts the name of a city and its country
# the function shall print a simple sentence, e.g. "'City' is in 'country'"
# parameter for the country to be a default value
# call function for three different cities, at least one of which is not in the default country

def describe_city(city, country='France'):
    print(f"{city.title()} is in {country}.")
describe_city("Nice")
describe_city("Narbonne")
describe_city("Oslo") # this is the odd one that is not in the default country