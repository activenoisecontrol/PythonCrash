import json

def get_stored_number(user):
    """Get stored number by username if available."""
    filename = f'{user}_fav_num.json'
    try:
        with open(filename) as f:
            fav_numb = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_numb

def get_new_number(user):
    """Prompt for a new number for new user."""
    print(f"It's seems that you're new here, {user.title()}!")
    fav_numb = input("Tell me you favorite number and I'll remember it.\n>> ")
    filename = f'{user}_fav_num.json'
    with open(filename, 'w') as f:
        json.dump(fav_numb, f)

def greet_user():
    """Greet the user by name and return him his favorite number if available."""
    user = input("Input your username, and I'll return you your favorite number.\n>> ").lower()
    fav_numb = get_stored_number(user)
    if fav_numb:
        print(f"I know your favorite number, {user.title()}. It's {fav_numb}!")
    else:
        get_new_number(user)

greet_user()