'''
The contact portion of the ORM, contains classes for any sort of contact information (email, phone..)

Created on 03/08/2012

@author: Dor
'''
from sqlalchemy import Column, Integer, String
from socialmine.orm import main

class Email(main.Base):
    '''
    An email address
    '''
    __tablename__ = 'emails'
    id = Column(Integer, primary_key = True)
    email = Column(String)
    
class PhoneNumber(main.Base):
    '''
    A phone number
    '''
    __tablename__ = 'phones'
    id = Column(Integer, primary_key = True)
    number = Column(String)