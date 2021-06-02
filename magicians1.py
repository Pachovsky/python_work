magicians = ["erik", "courtney", "hendrix", "emala"]
the_great_magicians = []

def show_magicians(magicians):
    """Prints a list of magician names"""
    for magician in magicians:
        magician_names = magician.title()
        print(magician_names)

def make_great(magicians, the_great_magicians):
    for magician in magicians:
        while magicians:
            great_magician = magicians.pop()
            print("The great " + great_magician.title() + "!")
            the_great_magicians.append(great_magician)
show_magicians(magicians)
make_great(magicians[:], the_great_magicians)

print(magicians)
print(the_great_magicians)