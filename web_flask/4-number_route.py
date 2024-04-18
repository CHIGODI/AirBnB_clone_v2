#!/usr/bin/python3
""" This module conatins a simple Flask App """

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns simple string """
    return f'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns simple string """
    return f'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ returns simple string """
    if '_' in text:
        text = text.replace('_', ' ')
    return f'C {escape(text)}'

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text='is cool'):
    """ returns simple string with default ext or specified extention"""
    if '_' in text:
        text = text.replace('_', ' ')
    return f'Python {escape(text)}'

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ returns string if n is a number """
    return f'{escape(n)} is a number'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    