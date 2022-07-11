print("\n-----> Exercise 6-6 Pollings <-----\n")
# use the code in favourite_languages
# make a list of who should take the poll
# include names who are in the dictionary and some that are not
# loop through a list of people who should take the poll
# if they have taken the poll, print the message thanking them responding
# if they haven't taken the poll, print the message inviting them to take the poll
name_for_poll = ['anne', 'john', 'luc', 'kate', 'angela', 'eric', 'marie', 'lucy']
favourite_languages = {
    'anne':'german',
    'john':'english',
    'kate':'spanish',
    'eric':'english',
    'lucy':'spanish'
}
for name in name_for_poll:
    if name in favourite_languages.keys():
        print(f"Dear {name.title()}, thanks for participating in the language poll! 👏")
    else:
        print(f" *** Dear {name.title()}, please take the language poll by Saturday 31st December 2022!✨ *** ")
print("\n")