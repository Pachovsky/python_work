#slicing a list:
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#looping through a slice:
print("\nHere are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

#copying a list:
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

for food in my_foods:
    print(food)

for food in friend_foods:
    print(food)








