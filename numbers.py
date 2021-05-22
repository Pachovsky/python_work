#using the range() function:
for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)

#using range() to make a list of numbers:
numbers = list(range(1,6))
print(numbers)

#skipping numbers, output: [2, 4, 6, 8, 10]
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#squares:
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)
#same but shorter:
squares = []
for value in range(12, 22):
    squares.append(value**2)

print(squares)

#simple statistics with a list of numbers:
digits = list(range(0, 10))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehensions: does the same as code from line 24-28
squares = [value**2 for value in range(12, 22)]
print(squares)




