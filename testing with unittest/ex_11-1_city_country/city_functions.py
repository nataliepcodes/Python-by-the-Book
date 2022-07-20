# write a function that accepts two parameters, a city name and a country name
# the function should return a single string of the form City, Country, such as Santiago, Chile
# create a file called test_cities.py to test this fuction

def get_city_country(city, country):
    """Generate a string"""
    string = f"{city.title()}, {country.title()}"
    return string