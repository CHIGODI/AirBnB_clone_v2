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


@app.route('/states', strict_slashes=False)
def states_list():
    """ renders a list states and its cities """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def states(id=''):
    """ renders states based on provided id """
    if id:
        states = storage.all(State)
        for state in states.values():
            if state.id == id:
                return render_template('9-states.html',
                                       state=state, found=True)
            else:
                return render_template('9-states.html', found=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=1)
