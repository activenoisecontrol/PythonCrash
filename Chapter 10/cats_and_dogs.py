from os import read


def read_file(filename):
    """Read content of the file and print it."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        ### print(f"File {filename} not found.")
    else:
        print(f"{contents}\n")

files = ['cats.txt', 'dogs.txt']
for file in files:
    read_file(file)