
class Employee():

    def __init__(self, first, last, salary):
        """Initialize an employee instance."""
        self.first = first
        self.last = last
        self.salary = salary
    
    def give_raise(self, amount=5000):
        self.salary += amount
