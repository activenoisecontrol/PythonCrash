import json

def get_stored_name(filename):
    """Get stored name if available."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(filename):
    username = input("What is your name?\n>>")
    with open(filename, 'w') as f:
            json.dump(username, f)
            return username

def greet_user(filename):
    """Greeting user"""
    username = get_stored_name(filename)
    if username:
        print(f"Welcome back {username}!")
    else:
        username = get_new_username(filename)
        print(f"We'll remember you when you come back, {username}!")

filename = 'usernamess2.json'
greet_user(filename)