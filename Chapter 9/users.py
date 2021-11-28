class User:
    """A simple attempt to creat a user."""
    
    def __init__(self, fi_name, la_name):
        """Initialize attributes to describe a user."""
        self.fi_name = fi_name.title()
        self.la_name = la_name.title()
        self.fu_name = f"{self.fi_name} {self.la_name}"
        self.login_attempts = 0

    def greet_user(self):
        """Print greetings for every user."""
        print(f"Hello {self.fu_name}. You have {self.login_attempts} login attempts.")

    def increment_login_attempts(self):
        """Increment loggin attempts value by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts value to 0."""
        self.login_attempts = 0

class Privileges():
    """Define privileges"""
    def __init__(self):
        self.privileges = ("can add post", "can delete post", "can ban user")

class Admin(User):
    """Used to create Admins"""
    def __init__(self, fi_name, la_name, level = 'user'):
        super().__init__(fi_name, la_name)
        self.level = level
        self.privileges = Privileges()
    
    def show_privileges(self):
        if self.level == 'user':
            print(f"You are a {self.level} and you can:")
            priv = self.privileges.privileges[0:2]
            for p in priv:
                print(f"- {p}")
        
        elif self.level == 'admin':
            print(f"You are an {self.level.upper()} and YOU CAN:")
            for p in self.privileges.privileges:
                print(f"- {p}")


