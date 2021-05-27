# looping through all key-value pairs

user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

for name, language in favorite_languages.items():
    print("\n" + name.title() + "'s favorite language is: " +
          language.title() + ".")

print("\n")
# Looping through all the keys in a dictionary
for name in favorite_languages.keys():
    print(name.title())

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\n")
# looping through a dictionary's keys in order

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("\n")
# looping through all values in a dictionary

print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

print("\n")

# to remove repetition you use a "set"
for language in sorted(set(favorite_languages.values())):
    print(language.title())

print("\n")
# 6-6 Polling
should_poll_names = ["jen", "edward", "colin", "joy", "caitlin"]
for should_poll_name in should_poll_names:
    if should_poll_name in favorite_languages:
        print("Thank you " + should_poll_name.title() + " for responding.")
    else:
        print("Please take the poll " + should_poll_name.title() + ".")

