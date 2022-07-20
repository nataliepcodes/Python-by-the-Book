# modify ex 11-1 function to add a third parameter 'population'
# it should now return a single string 'Santiago, Chile - population 5000000
# modify the function so that the population paramenter is optional

def get_city_country(city, country, population=''):
    """Return a string"""
    if population:
        string = f"{city.title()}, {country.title()} - population {population}"
    else: 
        string = f"{city.title()}, {country.title()}"
    return string