# store information about a pizza being ordered
# a list in a dictionary
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

# summarize the order
print("You ordered a " + pizza["crust"] + "-crust pizza with the following toppings:")

for topping in pizza["toppings"]:
    print("\t" + topping)

print("\n")
# favorite languages:

favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    else:
        print("\n" + name.title() + "'s favorite language is:")
        for language in languages:
            print("\t" + language.title())

print("\n")
# a dictionary in a dictionary

users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]

    print("\tFull names: " + full_name.title())
    print("\tLocation: " + location.title())