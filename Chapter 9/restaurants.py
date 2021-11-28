class Restaurant:
    """Creates restaurants"""
    def __init__(instance, name, cuisine):
        """Define each instance name and cuisine"""
        instance.name = name
        instance.cuisine = cuisine
        instance.number_served = 0 
    
    def describe_restaurant(instance):
        """Gives small description about restaraunt"""
        print(f"Welcome to the {instance.name.title()} restaurant with {instance.cuisine.title()} cuisine")

    def open_restaurant(instance):
        """Indicate that the restaurant is open"""
        print(f"{instance.name.title()} is open")

    def set_number_served(instance, num):
        """Set number of customers."""
        instance.number_served = num
    
    def increment_number_served(instance, plus):
        """Increment number of customers"""
        instance.number_served += plus

class IceCreamStand(Restaurant):
    """Creat special Ice Cream Stand Restaurant"""
    def __init__(self, name, cuisine = "ice cream"):
        super().__init__(name, cuisine)
        self.flavors = ('gum', 'stawberry', 'cherry')
    
    def display_flavors(self):
        print(f"Welcome to the {self.name} ice-cream restaurant")
        print("We can offer you next ice-creams listed below:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
