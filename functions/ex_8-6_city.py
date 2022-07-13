# write a function called city_country(), it takes the name of the city and country
# return a string formatted like this: "Santiago, Chile"
def city_country(city, country):
    """Return the name of the city and country as a string"""
    string = f"{city}, {country}"
    return string.title()

city_country_string = city_country("santiago", "chile")
print(city_country_string)
city_country_string = city_country("geneva", "switzerland")
print(city_country_string)
