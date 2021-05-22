pizzas =["Pizza Margaritha", "Pizza Döner", "Pizza Shoarma"]
for pizza in pizzas:
    print("I like " + pizza)

print("I really love pizza!")

friend_pizzas = pizzas[:]

pizzas.append("Pizza Pollo")
friend_pizzas.append("Pizza Tonno")

print("\nMy favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\nMy friends favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)