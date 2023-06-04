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
         
    def num_reviews(self):
        engine = create_engine('sqlite:///review.db')
        Session = sessionmaker(bind=engine)
        session = Session()  
        number_reviews = session.query(Review).filter(Review.restaurant_customer ==self.first_name).count()              
        return number_reviews
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if f'{customer.first_name} {customer.surname}' == name:
                return customer.first_name
            else:
                return "customer not found"  
                          
    @classmethod      
    def find_all_given_name(cls, name):
        for customer in cls.all_customers:
            if customer.first_name == name:
                return customer.first_name
            else:
                return 'Names not available.'

                
Base.metadata.create_all(engine)



    
           
    


    

         
     
           
