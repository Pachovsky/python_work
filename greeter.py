# user input
# writing clear prompts
name = input("Please enter your name: ")
print("Hello, " + name + "!")

# storing your prompt in a variable and pass that variable to the input() function:
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

# Using int() to Accept Numerical Input
age = input("How old are you? ")
print(age)