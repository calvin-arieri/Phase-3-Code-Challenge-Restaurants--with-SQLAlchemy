from sqlalchemy import String, Integer, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Customer import Customer
from Restaurant import Restaurant

engine = create_engine('sqlite:///review.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Review(Base):
    __tablename__ = 'reviews'

    review_id = Column(Integer, primary_key = True)
    restaurant = Column(String)
    restaurant_customer = Column(String)
    customer_rating = Column(String)
    

    all_reviews = []
    def __init__(self, restaurant, restaurant_customer, customer_rating):
        self.restaurant_ = restaurant
        self.restaurant_customer = restaurant_customer
        self.customer_rating = customer_rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.customer_rating
    
    @classmethod
    def all(cls):
        for review in cls.all_reviews:
            return review

    def customer(self):
        engine = create_engine('sqlite:///customer.db')
        Session = sessionmaker(bind=engine)
        session =Session()
        reviewing_customers = session.query(Customer).all()
        for theCustomer in reviewing_customers:
            if theCustomer.first_name == self.restaurant_customer:
                return theCustomer
            else:
                return "customer not found"
            
    def restaurant(self):
        engine = create_engine('sqlite:///restaurant.db')
        Session = sessionmaker(bind=engine)
        session =Session()
        restaurant_reviewed = session.query(Restaurant).all()
        for theRestaurant in restaurant_reviewed:
            if theRestaurant.restaurant_name == self.restaurant_:
                return theRestaurant
            else:
                return 'The restaurant not found'
            

Base.metadata.create_all(engine)
    

        
    


