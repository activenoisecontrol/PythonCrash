import json

with open('fav_num.json') as f:
    fav_numb = json.load(f)

print(f"I know your favorite number. It's {fav_numb}")