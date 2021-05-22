guest_list = ["Hans", "Joyce", "Colin", "Caitlin"]
print(guest_list[0] + ", I'd like to invite you to dinner.")
print(guest_list[1] + ", I'd like to invite you to dinner.")
print(guest_list[2] + ", I'd like to invite you to dinner.")
print(guest_list[3] + ", I'd like to invite you to dinner.")

print(guest_list[2] + " can't make it.")

guest_list[2] = "Joy"
print(guest_list[0] + ", I'd like to invite you to dinner.")
print(guest_list[1] + ", I'd like to invite you to dinner.")
print(guest_list[2] + ", I'd like to invite you to dinner.")
print(guest_list[3] + ", I'd like to invite you to dinner.")

print("I have found a bigger dinner table.")

guest_list.insert(0, "Cees")
guest_list.insert(3, "Mike")
guest_list.append("Brian")

print(guest_list)

print(guest_list[0] + ", I'd like to invite you to dinner.")
print(guest_list[1] + ", I'd like to invite you to dinner.")
print(guest_list[2] + ", I'd like to invite you to dinner.")
print(guest_list[3] + ", I'd like to invite you to dinner.")
print(guest_list[4] + ", I'd like to invite you to dinner.")
print(guest_list[5] + ", I'd like to invite you to dinner.")
print(guest_list[6] + ", I'd like to invite you to dinner.")

print("I can only invite two people for dinner.")

brian_pop = guest_list.pop(6)
print("I'm sorry I can't invite you to dinner " + brian_pop + ".")
caitlin_pop = guest_list.pop(5)
print("I'm sorry I can't invite you to dinner " + caitlin_pop + ".")
mike_pop = guest_list.pop(3)
print("I'm sorry I can't invite you to dinner " + mike_pop + ".")
joyce_pop = guest_list.pop(2)
print("I'm sorry I can't invite you to dinner " + joyce_pop + ".")
hans_pop = guest_list.pop(1)
print("I'm sorry I can't invite you to dinner " + hans_pop + ".")

print(guest_list)

print("You're still invited " + guest_list[0] + ".")
print("You're still invited " + guest_list[1] + ".")

del guest_list[0]
del guest_list[1]

print(guest_list)















