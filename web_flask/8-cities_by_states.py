#!/usr/bin/python3
""" This module conatins a simple Flask App """

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def delete_session(exception=None):
    """"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ """
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
