# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

prompt = "\nEnter a pizza topping that you would like to add to your pizza: "
prompt += "\n(Enter 'quit' when you're done.)"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("I will add " + topping.title() + " to your pizza!")