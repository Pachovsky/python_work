
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

