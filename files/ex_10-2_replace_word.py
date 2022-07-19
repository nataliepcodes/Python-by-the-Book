# read each line from learning_python.txt and replace Python with C
# note, this replacement does not change the original file
filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line.rstrip())

# check that the original file did not change
with open('learning_python.txt') as file_object:
    content = file_object.read()
    print(content)


