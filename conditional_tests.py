name = "colin"
print("Is name == 'colin'? I predict True.")
print(name == "colin")

print("\nIs name == 'cees'? I predict False.")
print(name == "cees")

last_name = "pachovsky"
print("\nIs last_name == 'rouse'? I predict False.")
print(last_name == "rouse")

print("\nIs last_name == 'pachovsky'? I predict True.")
print(last_name == "pachovsky")

girlfriend = "joy"
print("\nIs girlfriend == 'joy'? I predict True.")
print(girlfriend == "joy")

print("\nIs girlfriend == 'maria'? I predict False.")
print(girlfriend == "maria")

girlfriend_last_name = "rouse"
print("\nIs girlfriend_last_name == 'pachovsky'? I predict False.")
print(girlfriend_last_name == "pachovsky")

print("\nIs girlfriend_last_name == 'rouse'? I predict True.")
print(girlfriend_last_name == "rouse")

monthly_income = 1160
print("\nIs monthly_income == 1160? I predict True.")
print(monthly_income == 1160)

print("\nIs monthly_income == 960? I predict False.")
print(monthly_income == 960)

print("\n")

car = "peugeot 206"
print(car)
if car == "peugeot 206":
    print("That is your car!")
else:
    print("That's not your car.")

car = "bmw m3"
if car != "peugeot 206":
    print("This is the wrong car!")

car2 = "BMW"
if car2.lower() == "bmw":
    print("This is a BMW.")
else:
    print("This is not a BMW.")

number = 18
if number == 17:
    print("This is number 17.")
else:
    print("This is not number 17.")

number = 34
if number > 17:
    print("This number is greater than 17.")
else:
    print("This number is less than 17.")

number = 6
if number >= 17:
    print("This number is greater than or equal to 17.")
else:
    print("This number is less than or equal to 17.")

fav_pizza = "Pizza Döner"
fav_pizza2 = "Pizza Shoarma"
if fav_pizza == "Pizza Döner" and fav_pizza2 == "Pizza Shoarma":
    print("These are your favorite pizzas.")
else:
    print("These are not your favorite pizzas.")

if fav_pizza != "Pizza Döner" or fav_pizza2 != "Pizza Shoarma":
    print("These are not your pizzas")
else:
    print("These are for sure your pizzas")

family = ["Joy", "Colin", "Caitlin", "Mark", "Hans", "Joyce"]
person = "Joy"
if person in family:
    print("This person belongs to your family")

person = "Henk"
if person not in family:
    print("This person does not belong to your family")
