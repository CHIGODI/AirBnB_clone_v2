#!/usr/bin/python3
""" This module conatins a simple Flask App """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns simple string """
    return f'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
