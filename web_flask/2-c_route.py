#!/usr/bin/python3
""" This module conatins a simple Flask App """

from flask import Flask


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
        return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    