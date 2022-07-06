# whitespace refers to a non-printing character
# e.g. spaces, tabs and end of line symbols

# to add a tab
print("\tPython")

print("---------------------------------")

# to add a newline
print("Languages:\nPython\nC\nJavascript")

print("---------------------------------")

# to a tab and a new line
print("Languages:\n\tJavascript\n\tC\n\tPython")

print("---------------------------------")
# stripping whitespace e.g "python " to "python"
# rstrip() method is used to remove a whitespace on the right side of the string
# lstrip() method is used to remove a whitespace on the left side of the string
# strip() method is used to remove a whitespace on both sides of the string

favourite_language = "python "
favourite_language = favourite_language.rstrip()
print(favourite_language)

favourite_language = " C"
favourite_language = favourite_language.lstrip()
print(favourite_language)

favourite_language = " JavaScript "
favourite_language = favourite_language.strip()
print(favourite_language)