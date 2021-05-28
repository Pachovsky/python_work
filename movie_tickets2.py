prompt = "\nTo receive your ticket price, please enter your age. "
prompt += "\n(Enter 'quit' when you're done. ): "

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False

    if int(age) < 3:
        print("The ticket is free!")
    elif int(age) < 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")

