# - `Restaurant __init__()`
#   - Restaurants should be initialized with a name, as a string
# - `Restaurant name()`
#   - returns the restaurant's name
#   - should not be able to change after the restaurant is created
class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name

    def name(self):
        return self.restaurant_name
    
