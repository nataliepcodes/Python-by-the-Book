# start with a copy of user_profile.py 
# build a profile of yourself by calling build_profile()
# using your first and last name and three other key-value pairs that describe you

# a function takes name and surname arguments, and creates an empty dictionary to store key-value pairs
def build_profile(name, surname, **kwargs):
    kwargs['name'] = name
    kwargs['surname'] = surname
    return kwargs


# created a variable to receive the dictionary for the passed arguments in the function call
my_profile = build_profile('natalie', 'peyre', location = 'europe', address = 'private information', age = 'prefer not to say')

# print a dictionary
print(my_profile)

