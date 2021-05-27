
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

# cities

