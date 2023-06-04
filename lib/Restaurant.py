from sqlalchemy import String, Integer, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
        the_reviews = engine.execute('SELECT * FROM reviews')
        for that_review in the_reviews:
            if that_review.restaurant == self.restaurant_name:
                return that_review
            else:
                return 'restaurant not found'

    def customers(self):
        engine = create_engine('sqlite:///review.db')
        the_reviews = engine.execute('SELECT * FROM reviews')
        customer_who_reviewed = []
        for that_review in the_reviews:
            if that_review.restaurant == self.restaurant_name:
                customer_who_reviewed.append(that_review.restaurant_customer) 
            else:
                return 'restaurant not found'
        return(set(customer_who_reviewed))    
                
    
Base.metadata.create_all(engine)   
    
