'''
Created on 03/08/2012

@author: Dor
'''
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker


engine = create_engine(r'sqlite://C:\mine.db')
Session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
Base = declarative_base()

class PersonalInformation(Base):
    '''
    Contains various types of personal information.
    May be the information from a single outlet or a subject amalgam of a few.
    '''
    __tablename__ = 'infos'
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    
class Person(Base):
    '''
    Represents a single person, linked to all of the person's online presence.
    '''
    __tablename__ = 'persons'
    id = Column(Integer, primary_key = True)
    info_id = Column(Integer, primary_key = True)
    info = relationship(PersonalInformation, primaryjoin = Person.info_id == PersonalInformation.id)
    
class Profile(Base):
    '''
    Represents a profile of a user in some outlet.
    '''
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key = True)
    type = Column(String)
    profile_value = Column(String)
    person_id = Column(Integer, ForeignKey(Person.id))
    person = relationship(Person, primaryjoin = Profile.person_id == Person.id)
    info_id = Column(Integer, primary_key = True)
    info = relationship(PersonalInformation, primaryjoin = Person.info_id == PersonalInformation.id)
    
class PresenceSample(Base):
    '''
    A sample of some online activity in some outlet for some user.
    '''
    __tablename__ = 'samples'
    id = Column(Integer, primary_key = True)
    time = Column(DateTime)
    description = Column(String)
    was_active = Column(Boolean)
    was_online = Column(Boolean)
    
class Post(Base):
    '''
    A general "post" class for any information posted by a user, seen in some sample.
    '''
    __tablename__ = 'posts'
    id = Column(Integer, primary_key = True)
    post = Column(String)
    sample_id = Column(Integer, primary_key = True)
    sample = relationship(PresenceSample, primaryjoin = Post.sample_id == PresenceSample.id)