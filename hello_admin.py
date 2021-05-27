# 5-8. Hello Admin. 5-9. No users.
usernames = ["colin", "admin"]

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello " + username + ", would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again.")
else:
    print("We need to find some users!")

print("\n")
# 5-10. Checking usernames.
current_users = ["colin", "joy", "caitlin", "hans", "joyce"]

new_users = ["Caitlin", "Hans", "cees", "mike", "brian"]

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", this username has already been used. Enter a new username.")
    else:
        print("Great " + new_user + ", this username is available.")

print("\n")
# 5-11. Ordinal Numbers.
numbers = list(range(1, 11))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")