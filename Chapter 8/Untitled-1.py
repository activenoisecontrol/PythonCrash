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

restaurant = Restaurant('Raviga', 'dutch')
restaurant.describe_restaurant()
print(f"Number of customers: {restaurant.number_served}")
restaurant.number_served = 13
print(f"Number of customers at the moment: {restaurant.number_served}")
restaurant.set_number_served(1321)
print(f"Number of customers at the moment: {restaurant.number_served}")
restaurant.increment_number_served(1)
print(f"Number of customers at the moment: {restaurant.number_served}")