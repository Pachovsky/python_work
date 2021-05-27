cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# checking for inequality:
requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")

# numerical comparisons:
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

# using "and" to check multiple conditions
age_0 = 22
age_1 = 18

if age_0 >= 21 and age_1 >= 21:
    print("It's legal to drink!")
else:
    print("You can't drink together")

# both old enough:
age_0 = 22
age_1 = 22

if age_0 >= 21 and age_1 >= 21:
    print("It's legal to drink!")
else:
    print("You can't drink together")

# using "or" to check multiple conditions:
age_0 = 18
age_1 = 22

if age_0 >= 21 or age_1 >= 21:
    print("Both, or just one of you can legally drink.")
else:
    print("Neither of you can drink.")

# checking whether a value is in a list using "in":
requested_toppings = ["mushrooms", "onions", "pineapple"]
if "mushrooms" in requested_toppings:
    print("This list contains mushrooms.")
else:
    print("This list does not contain mushrooms.")

if "pepperoni" in requested_toppings:
    print("This list contains pepperoni.")
else:
    print("This list does not contain pepperoni.")

# checking whether a value is not in a list
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")













