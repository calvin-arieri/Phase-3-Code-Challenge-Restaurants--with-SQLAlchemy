from sqlalchemy import String, Integer, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Review import Review

engine = create_engine('sqlite:///restaurant.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Restaurant(Base):
    __tablename__= 'restaurants'

    restaurant_id = Column(Integer, primary_key=True)
    restaurant_name = Column(String)

    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name

    def name(self):
        return self.restaurant_name
    
    def reviews(self):
        engine = create_engine('sqlite:///review.db')
        Session = sessionmaker(bind= engine)
        session = Session()
        the_reviews = session.query(Review).all() 
        for that_review in the_reviews:
            if that_review.restaurant_name == self.restaurant_name:
                return that_review
            else:
                return 'restaurant not found'

    def customers(self):
        engine = create_engine('sqlite:///review.db')
        Session = sessionmaker(bind= engine)
        session = Session()
        the_reviews = session.query(Review).all()
        customer_who_reviewed = []
        for that_review in the_reviews:
            if that_review.restaurant_name == self.restaurant_name:
                customer_who_reviewed.append(that_review.restaurant_customer) 
            else:
                return 'restaurant not found'
        return(set(customer_who_reviewed))    
                
    def  average_star_rating(self):
        

Base.metadata.create_all(engine)   
    
