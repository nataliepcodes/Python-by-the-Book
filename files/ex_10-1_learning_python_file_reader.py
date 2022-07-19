# write a program that reads the file and prints content of a file three times 
# once: by reading the entire file
# once: by looping over the file object
# once: by storing the items in a list and working outsite the 'with' block

print("\n............. reading the entire file .............\n")
filename = 'learning_python.txt'
with open(filename) as file_objects:
    contents = file_objects.read()
    print(contents.rstrip())

print("\n............. looping over a file object .............\n")
filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n............. storing the items in a list and working outsite the 'with' block .............\n")
filename = 'learning_python.txt'
with open(filename) as file_object:
    list = file_object.readlines()

for line in list:
    print(line.rstrip())
