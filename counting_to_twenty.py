for value in range(1,21):
    print(value)

numbers = list(range(1,1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers1 = list(range(1,20,2))
for number in numbers1:
    print(number)

multiples = list(range(3,33,3))
for multiple in multiples:
    print(multiple)

cubes = [value**3 for value in range(1,10)]
print(cubes)



