#!/usr/bin/python3
""" This module conatins a simple Flask App """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def delete_session(exception=None):
    """ Close a sqlalchemy session connected to db """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ renders a list states and its cities """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
