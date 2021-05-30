def city_country(city, country):
    """Function that tells in which country a city is."""
    city_and_country = city + ", " + country
    return city_and_country.title()

city1 = city_country("amsterdam", "the netherlands").title()
city2 = city_country("santiago", "chile").title()
city3 = city_country("berlin", "germany").title()
print(city1 + "\n" + city2 + "\n" + city3 + "\n")