
pets = {
    "miauw": {
        "species": "cat",
        "owners_name": "mike"
    },
    "rakker": {
        "species": "dog",
        "owners_name": "colin"
    },
    "piccolo": {
        "species": "horse",
        "owners_name": "jennifer"
    },
}

for pet, pet_info in pets.items():
    print(pet.title() + " is a " + pet_info["species"] + " and its owner is " + pet_info["owners_name"].title() + ".")

# favorite places

print("\n")

favorite_places = {
    "colin": ["colorado", "washington", "france"],
    "joy": ["the netherlands", "spain"],
    "mark": ["china", "greece"]
}

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places are: ")
    for place in places:
        print("\t" + place.title())

# favorite numbers 

print("\n")

favorite_numbers = {
    "colin": [13, 22],
    "joy": [24, 76],
    "hans": [15],
    "mike": [27, 45, 69],
    "brian": [66, 83],
    "caitlin": [29],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(name.title() + "'s favorite numbers are: ")
        for number in numbers:
            print("\t" + str(number))
    else:
        print(name.title() + "'s favorite number is: ")
        for number in numbers:
            print("\t" + str(number))

print("\n")
# cities

cities = {
    "naples": {
        "country": "italy",
        "population": 3085000,
        "fact": "Naples, a city in southern Italy, sits on the Bay of Naples. \
Nearby is Mount Vesuvius, the still-active volcano that destroyed nearby Roman town Pompeii. \
Dating to the 2nd millennium B.C., Naples has centuries of important art and architecture. \
The city's cathedral, the Duomo di San Gennaro, is filled with frescoes. \
Other major landmarks include the lavish Royal Palace and Castel Nuovo, a 13th-century castle.\n",
    },
    "amsterdam": {
        "country": "the netherlands",
        "population": 821752,
        "fact": "Amsterdam is the Netherlands’ capital, known for its artistic heritage, \
elaborate canal system and narrow houses with gabled facades, legacies of the city’s 17th-century Golden Age. \
Its Museum District houses the Van Gogh Museum, works by Rembrandt and Vermeer at the Rijksmuseum, \
and modern art at the Stedelijk. Cycling is key to the city’s character, and there are numerous bike paths.\n",
    },
    "seatle": {
        "country": "the united states of america",
        "population": 724305,
        "fact": "Seattle, a city on Puget Sound in the Pacific Northwest, is surrounded by water, \
mountains and evergreen forests, and contains thousands of acres of parkland. \
Washington State’s largest city, it’s home to a large tech industry, with Microsoft \
and Amazon headquartered in its metropolitan area. The futuristic Space Needle, a 1962 World’s Fair legacy, \
is its most iconic landmark.\n",
    },
}

print("Here is some information about my favorite cities: \n")
for city, city_info in cities.items():
    print(city.title() + ": \n\t" + "Country: " + city_info["country"].title() + "." + "\n\tPopulation: " +
    str(city_info["population"]) + "." + "\n\tFact: " + city_info["fact"].title())

    