#defining a tuple:
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#looping through all values in a tuple:
for dimension in dimensions:
    print(dimension)

#writing over a tuple:
dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)

print("\n")
simple_foods = ("fries", "chicken", "spinach", "burritos", "macaroni")
for food in simple_foods:
    print(food)

print("\n")
simple_foods = ("patat", "chicken", "spinazie", "burritos", "macaroni")
for food in simple_foods:
    print(food)
