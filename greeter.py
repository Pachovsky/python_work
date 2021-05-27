# user input
# writing clear prompts
name = input("Please enter your name: ")
print("Hello, " + name + "!")

# storing your prompt in a variable and pass that variable to the input() function:
prompt = "If you tell me who you are, I can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

# Using int() to Accept Numerical Input
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You are 18+! Your age is: " + str(age))

# rollercoaster
height = input("How tall are you in centimeters? ")
height = int(height)

if height >= 120:
    print("\nYou are tall enough to ride the rollercoaster!")
else:
    print("\nYou'll be able to ride when you are a little older.")

# the modulo operator
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# 7-1 rental car
car = input("What kind of rental car would you like? ")
print("\nLet me see if I can find a " + car + " for you!")

print("\n")
# 7-2 restaurant seating
seats = input("How many people are in your dinner group? ")
seats = int(seats)

if seats > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")