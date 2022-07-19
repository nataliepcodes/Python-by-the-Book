# open() opens the argument that is the file and returns an object that is assigned to the file_object
with open('pi_digits.txt') as file_object:
    # read() reading the file and storing the contents in the contents variable
    # read() returns an empty string when it reaches the EOF
    contents = file_object.read()
print(contents) #to remove empty string use rstrip() print(contents.rstrip())

# reading line by line and removing blank lines
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())