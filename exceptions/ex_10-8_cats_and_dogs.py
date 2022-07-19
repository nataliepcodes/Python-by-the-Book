# make two files cats.txt and dogs.txt
# store at least 3 names of cats in the cats file
# store at least 3 names of dogs in the dogs file
# write the program that reads these files and tries to print the contents to the screen
# write your code in a try-except block to catch the FileNotFoundError and print a friendly message if a file is missing
# move one of the files to a different location and make sure the code executes properly

def read_files(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, {filename} file does not exist.")
    else:
        print("------------------------------------")
        print(f"File {filename} contents are: \n{contents}")
    
files = ['cats.txt', 'dogs.txt']
for file in files:
    read_files(file)
    print("------------------------------------")
