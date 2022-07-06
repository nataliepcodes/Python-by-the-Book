# f-strings, f is for format
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(full_name)

# use f-string to compose complete messages
print(f"Hello, {full_name.title()}")

# use f-strings to compose message and assign message to a variable
message = f"Hello, {full_name.title()}"
print(message)