# modify except block from ex 10-8 to fail silently if either file is missing

def read_files(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"File {filename} contents are: \n{contents}")
    
files = ['cats.txt', 'dogs.txt']
for file in files:
    read_files(file)
