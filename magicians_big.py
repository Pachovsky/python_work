def show_magicians(names):
    for name in names:
        msg = "Magician: " + name.title() + "."
        print(msg)

magicians = ["colin", "mike"]
show_magicians(magicians)