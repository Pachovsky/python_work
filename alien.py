alien_0 = {"color": "green", "points": 5}
# accessing values in a dictionary
print(alien_0["color"])
print(alien_0["points"])

new_points = alien_0["points"]
print("You just earned " + str(new_points) + " points!")

# adding new key-value pairs
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print("alien_0:")
print(alien_0)

print("\n")
# starting with an empty dictionary
alien_1 = {}

alien_1["color"] = "yellow"
alien_1["points"] = 10

print("alien_1:")
print(alien_1)

print("\n")

# modifying values in a dictionary
print("The alien is " + alien_0["color"] + ".")

alien_0["color"] = "yellow"
print("The alien is now " + alien_0["color"] + ".")

print("\n")

# second example:

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print("Original x-position: " + str(alien_0["x_position"]))

# move the alien to the right.
# determine how far to move the alien based on its current speed.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # this must be a fast alien.
    x_increment = 3

# the new position is the old position plus the increment.
alien_0["x_position"] = alien_0["x_position"] + x_increment

print("New x-position: " + str(alien_0["x_position"]))

print("\n")
# removing key-value pairs
alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)

print("\n")
# a dictionary of similar objects
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

print("Sarah's favorite language is " +
      favorite_languages["sarah"].title() + "."
      )
