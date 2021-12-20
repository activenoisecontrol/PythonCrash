import json

#user = input("Input your username, and I'll return you your favorite number.")
filename = 'fav_numb.json'     # = f'{}_fav_num.json'

try:
    with open(filename) as f:
        fav_numb = json.load(f)
except FileNotFoundError:
    fav_numb = input("Hi! What is your favorite number?\n>>")
    with open(filename, 'w') as f:
        json.dump(fav_numb, f)
else:
    print(f"I know your favorite number. It's {fav_numb}")
