locations = ["Norway", "China", "Egypt", "Sweden", "Brazil"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

#exercise 3.9
guest_list2 = ["Hans", "Joyce", "Colin", "Caitlin"]
print(len(guest_list2))

#Every function
color_list = ["Red", "Blue", "Yellow", "Green", "Purple", "Grey", "Brown", "Pink", "Black", "White"]
print(color_list)
print(color_list[2])
print(color_list[2].upper())
print(color_list[-1])

message1 = "My favorite color is: " + color_list[-2] + "."
print(message1)

color_list[0] = "Rood"
print(color_list)
color_list[0] = "Red"
print(color_list)

color_list.append("Navy Blue")
print(color_list)

color_list.insert(3, "Army Green")
print(color_list)

del color_list[3]
print(color_list)

popped_color = color_list.pop(-1)
print("I will remove this color from the list: " + popped_color + ".")
print(color_list)

color_list.remove("Red")
print(color_list)

too_naturish = "Green"
color_list.remove(too_naturish)
print(color_list)
print("\n\tThis is definitely not my favorite color: " + too_naturish + ".")

print("\nHere is the original list: ")
print(color_list)
print("\nHere is the sorted list: ")
print(sorted(color_list))

print("\n")
color_list.sort()
print(color_list)

color_list.sort(reverse=True)
print(color_list)

color_list.sort(reverse=False)
print(color_list)

color_list.reverse()
print(color_list)
color_list.reverse()
print(color_list)

print("length of the list is: " + str(len(color_list)))







