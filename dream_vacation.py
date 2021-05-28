dream_vacations = {}

polling_active = True

while polling_active:
    name = input("Please enter your name: ")
    dream_vacation = input("If you could visit one place in the world, where would you go? ")

    dream_vacations[name] = dream_vacation

    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == "no":
        polling_active = False

print("\nDream Vacations: ")
for name, dream_vacation in dream_vacations.items():
    print(name.title() + "'s dream vacation is " + dream_vacation.title() + ".")