#Strings:
#Changing Case in a String with Methods:
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#Combining or Concatenating Strings:
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)

#Adding Whitespace to Strings with Tabs or Newlines:
print("Python")
#tab:
print("\tPython")
#newline:
print("Languages:\nPython\nC\nJavaScript")
#newline + tab:
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Stripping Whitespace in terminal:
favorite_language = " python "
favorite_language.rstrip()
#" python"
favorite_language.lstrip()
#"python "
favorite_language.strip()
#"python"









