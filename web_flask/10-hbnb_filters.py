#!/usr/bin/python3
""" This module conatins a simple Flask App """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def delete_session(exception=None):
    """ Close a sqlalchemy session connected to db """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def states_list():
    """ renders a list states and its cities """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
