print("\n-----> Exercise 6-10 Favourite Numbers <-----\n")
# modify your program from 6-2 so each person can have more than 1 favourite number
# print each person's name along with their fav number
favourite_numbers = {
    'anne' : [5, 3, 4], 
    'john' : [10, 1, 4],
    'peter': [3, 5, 6],
    'lucy' : [2, 7, 9],
    'rufus': [3, 2, 1]
}
for name, numbers in favourite_numbers.items():
    print(f"\n{name.title()}'s favourite numbers are:")
    for number in numbers:
     print(number) 

