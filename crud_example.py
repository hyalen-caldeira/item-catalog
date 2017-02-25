from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

def create(restaurant):
    session.add(restaurant)
    session.commit

def update():
    # Find Entry
    # Reset value(s)
    # Add to session
    # Execute session.commit()

    veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')

    for veggieBurger in veggieBurgers:
        print veggieBurger.name
        print veggieBurger.id
        print veggieBurger.price
        print veggieBurger.restaurant.name
        print "\n"

# def delete():
    # Find the entry
    # Session.delete(Entry)
    # Session.commit()

update()