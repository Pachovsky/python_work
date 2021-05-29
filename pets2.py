# positional arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("hamster", "harry")

# multiple function calls

describe_pet("dog", "willie")

# Keyword Arguments

describe_pet(animal_type="hamster", pet_name="harry")

# order of keyword arguments doesn't matter:

describe_pet(pet_name="willie", animal_type="dog")

# Default Values

def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name="willie")
describe_pet("xavi")
# different animal
describe_pet(animal_type="fish", pet_name="nemo")

# Avoiding Argument Errors

describe_pet()