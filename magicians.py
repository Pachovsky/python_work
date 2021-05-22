#looping through an entire list:
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

#doing more work within a for loop:
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

#doing something after a for loop
print("Thank you, everyone. That was a great magic show!")




















