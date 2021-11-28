favourite_fruits = ['apple', 'banana', 'peach']
asked_fruits = ['apple', 'banana', 'pear', 'lemon', 'apricot']

for fruit in favourite_fruits:
    if fruit in asked_fruits:
        print(f'You really like {fruit}s!')