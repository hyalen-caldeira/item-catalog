# Database setup consist of:
#   . Import the libraries and configure
#   . Class and table definition
#   . Mapping definition

### Configuration
import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

### Class Definition

class Restaurant(Base):
    ### Table Definition
    __tablename__ = 'restaurant'
    ## Columns
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)

class MenuItem(Base):
    __tablename__ = 'menu_item'
    ## Columns
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship('Restaurant')

### Create the DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)

