from flask import Flask
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB ##
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

app = Flask(__name__)

# http://flask.pocoo.org/docs/0.10/quickstart/#routing
# @app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_menu(restaurant_id):
    # restaurant = session.query(Restaurant).first()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)

    output = ''

    for item in items:
        output += item.name
        output += '</br>'
        output += item.price
        output += '</br>'
        output += item.description
        output += '</br>'
        output += '</br>'
        output += '</br>'

    return output

# Create route for newMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
    return "Page to create a new menu item  ..."

# Create route for editMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "Page to edit a menu item ..."

# Create a route for deleteMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "Page to delete a menu item ..."

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)