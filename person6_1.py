

# 6-2 favorite numbers
favorite_numbers = {
    "Colin": 13,
    "Joy": 24,
    "Mike": 27,
    "Brian": 66,
    "Caitlin": 29,
}

print("Colin's favorite number is: " +
      str(favorite_numbers["Colin"]) +
      ".")
print("Joy's favorite number is: " +
      str(favorite_numbers["Joy"]) +
      ".")
print("Mike's favorite number is: " +
      str(favorite_numbers["Mike"]) +
      ".")
print("Brian's favorite number is: " +
      str(favorite_numbers["Brian"]) +
      ".")
print("Caitlin's favorite number is: " +
      str(favorite_numbers["Caitlin"]) +
      ".")
print("\n")
# 6-3 Glossary
glossary = {
    "complain": "to express dissatisfaction, pain, uneasiness, censure, resentment, or grief; find fault",
    "grief": "keen mental suffering or distress over affliction or loss",
    "suffering": "the state of a person or thing that suffers",
    "suffer": "to undergo or feel pain or distress",
    "injury": "harm or damage that is done or sustained",
}

print("Complain: " + glossary["complain"].title() + ".")
print("Grief: " + glossary["grief"].title() + ".")
print("Suffering: " + glossary["suffering"].title() + ".")
print("Suffer: " + glossary["suffer"].title() + ".")
print("Injury: " + glossary["injury"].title() + ".")

print("\n")
# This does the same through looping:
for word, meaning in glossary.items():
    print(word.title() + ": " + meaning.title() + ".")

print("\n")
# rivers
rivers = {
    "nile": "egypt",
    "rijn": "the netherlands",
    "colorado river": "the united states of america",
}

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

print("\n")
# 6-1 and 6-7. People

people = {
    "person_1": {
        "first_name": "Joy",
        "last_name": "Rouse",
        "age": 44,
        "city": "Camas",
    },
    "person_2": {
        "first_name": "Colin",
        "last_name": "Pachovsky",
        "age": 24,
        "city": "Zuid-Beijerland",
    },
    "person_3": {
        "first_name": "Mike",
        "last_name": "Bezemer",
        "age": 25,
        "city": "Numansdorp"
    },
}

for key, person_info in people.items():
    print("Person's name: " + person_info["first_name"] + " " + person_info["last_name"] + ".")
    print("Is " + str(person_info["age"]) + " years old.") 
    print("And lives in " + person_info["city"] + ".\n")


# print(person_1["first_name"] + " " + person_1["last_name"] +
     # " is " + str(person_1["age"]) + " years old and lives in " +
     # person_1["city"] + "."
     # 
# )
