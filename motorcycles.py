motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#modifying elements in a list
motorcycles[0] = 'ducati'
print(motorcycles)

#appending elements to the end of a list
motorcycles.append('aprillia')
print(motorcycles)

motorcycles1 = []
motorcycles1.append('honda')
motorcycles1.append('suzuki')
motorcycles1.append('yamaha')
print(motorcycles1)

#inserting elements into a list
motorcycles1.insert(1, 'bmw')
print(motorcycles1)

#removing an item using the del statement
del motorcycles1[2]
print(motorcycles1)

#removing an item using the pop() method
last_owned_motorcycle = motorcycles1.pop()
print(motorcycles1)
print(last_owned_motorcycle)

print("The last motorcycle I owned was a " + last_owned_motorcycle.title() + ".")


motorcycles2 = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles2.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#removing an item by value

motorcycles3 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles3)
motorcycles3.remove('ducati')
print(motorcycles3)

too_expensive = 'honda'
motorcycles3.remove(too_expensive)
print(motorcycles3)
print("\nA " +  too_expensive.title() + " is too expensive for me.")






