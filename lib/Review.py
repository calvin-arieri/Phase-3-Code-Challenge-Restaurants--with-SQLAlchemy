from sqlalchemy import String,
class Review:
    all_reviews = []
    def __init__(self, restaurant, customer, customer_rating):
        self.restaurant = restaurant
        self.customer = customer
        self.customer_rating = customer_rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.customer_rating
    
    @classmethod
    def all(cls):
        for review in cls.all_reviews:
            return review

    def customer():

