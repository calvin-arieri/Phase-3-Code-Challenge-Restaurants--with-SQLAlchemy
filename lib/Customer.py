from sqlalchemy import String, Integer, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Review import Review

engine = create_engine('sqlite:///customer.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    surname = Column(String)
    
    all_customers = []

    def __init__(self, first_name, surname):
          self.first_name = first_name
          self.surname = surname
          Customer.all_customers.append(self)

    def given_name(self):
         return self.first_name
    
    def family_name(self):
         return self.surname
    
    def full_name(self):
         fullname = self.first_name + " " + self.surname
         return fullname
    
    @classmethod
    def all(cls):
       return cls.all_customers 
    
    def restaurants(self):
        engine = create_engine('sqlite:///review.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        the_reviews = session.query(Review).all()
        restaurants_reviewed = []
        for that_review in the_reviews:
            if that_review.restaurant_customer == self.first_name:
                restaurants_reviewed.append(that_review.restaurant) 
            else:
                return 'restaurant not found'
        return(set(restaurants_reviewed))
         
    
    def add_review(self, restaurant_, rating):
        engine = create_engine('sqlite:///review.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        new = Review(restaurant_name =restaurant_, customer_rating=rating, restaurant_customer= self.first_name)
        session.add(new)
        session.commit()
        session.close()
         
                
         
Base.metadata.create_all(engine)



    
           
    


    

         
     
           
