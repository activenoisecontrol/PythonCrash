def count_words(filename):
    try:
        with open(filename, encoding= 'utf8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File {filename} not found.")
    else:
        coun = contents.lower().count(' the ')
        print(coun)

files = ['the_heritage.txt', 'great_leaders.txt', 'saints_city.txt', 'godfather.txt']

for file in files:
    count_words(file)

