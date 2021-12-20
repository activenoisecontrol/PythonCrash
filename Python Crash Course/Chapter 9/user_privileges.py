from users import User

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
