#Sorting a list permanently with the sort() method:
cars = ["bwm", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

#sorting a list temporarily with the sorted() function
print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)

print(sorted(cars, reverse=False))

#Printing a list in reverse order:
cars1 = ["bwm", "audi", "toyota", "subaru"]
print(cars1)

cars1.reverse()
print(cars1)

#changing it back to original:
cars1.reverse()
print(cars1)

#Finding the length of a list:
print(len(cars1))