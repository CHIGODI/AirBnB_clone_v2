#!/usr/bin/python3
""" This module conatins a simple Flask App """

from flask import Flask, render_template
from markupsafe import escape
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ renders a list of states """
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def delete_session(exception=None):
    """ ends a  session/ deletes it to create a new one"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
