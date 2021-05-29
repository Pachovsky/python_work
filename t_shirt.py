def make_shirt(size, message):
    """Function to describe a t-shirt."""
    print("\nThis " + size.upper() + " size t-shirt has a message written on it, saying: " + message.capitalize())

make_shirt("m", "we love python!")
make_shirt(message="the earth is flat.", size="l")

# big shirts

def make_shirt(size="l", message="I love python"):
    """Function to describe a t-shirt."""
    print("\nThis " + size.upper() + " size t-shirt has a message written on it, saying: " + message.capitalize())

make_shirt()
make_shirt(size="m")
make_shirt(size="s", message="don't drink and drive!")