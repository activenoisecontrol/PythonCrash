import car as c
import my_car as e


my_tesla = e.ElectricCar('tesla', ' model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_beetle = c.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())