#!/usr/bin/python3
""" This module conatins a simple Flask App """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User


app = Flask(__name__)


@app.teardown_appcontext
def delete_session(exception=None):
    """ Close a sqlalchemy session connected to db """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def states_list():
    """ renders a list states and its cities """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    users = storage.all(User)
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           users=users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=1)
