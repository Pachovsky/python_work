# introducing while loops
# the while loop in action
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("\n")
# Using continue in a Loop
current_number1 = 0
while current_number1 < 10:
    current_number1 += 1
    if current_number1 % 2 == 0:
        continue

    print(current_number1)

print("\n")
# Avoiding Infinite Loops

x = 0
while x <= 8:
    print(x)
    x += 1