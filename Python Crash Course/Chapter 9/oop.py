import datetime

class Employee:

    def __init__(self, first, last, pay, raiseamount = 1.04):
        self.first = first.title()
        self.last = last.title()
        self.pay = pay
        self.email = f"{first}.{last}@company.com".lower()
        self.raiseamount = raiseamount
    
    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self, raiseamount = 1.04):
        self.raiseamount = raiseamount
        self.pay = self.pay * self.raiseamount
        return int(self.pay)

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

class Developer(Employee):

    def __init__(self, first, last, pay, language, raiseamount = 1.10):
        super().__init__(first, last, pay, raiseamount)
        self.language = language


st1 = 'John-Doe-70000'
new_emp1 = Developer('alek', 'bolduin', 60000, 'python')
print(new_emp1.raiseamount)

print(new_emp1.__dict__)

my_date = datetime.date(2021, 11, 26)
print(my_date)
print(Employee.is_workday(my_date))