# - `Customer __init__()`
#   - Customer should be initialized with a given name and family name, both strings (i.e., first and last name, like George Washington)"
# - `Customer given_name()`
#   - returns the customer's given name
#   - should be able to change after the customer is created
# - `Customer family_name()`
#   - returns the customer's family name
#   - should be able to change after the customer is created
# - `Customer full_name()`
#   - returns the full name of the customer, with the given name and the family name concatenated, Western style.
# - `Customer all()`
#   - returns **all** of the customer instances
from sqlalchemy import String, Integer, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///customer.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column()
    
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
         




    
           
    


    

         
     
           
