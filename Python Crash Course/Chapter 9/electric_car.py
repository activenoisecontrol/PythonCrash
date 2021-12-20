from car import Car

class Battery():
    def __init__(self, capacity):
        """Define battery"""
        self.capacity = capacity
    
    def get_range(self):
        if self.capacity == 75:
            range = 260
        elif self.capacity == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.") 
    
    def upgrade_battery(self):
        """Increase battery capacity."""
        if self.capacity == 75:
            self.capacity = 100

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, capacity = 75):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery(capacity)

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery.capacity}-kWh battery.")

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def fill_gas_tank(self):
        print("Electric car doesn't have gas tank")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()

print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.get_range()


