#!/usr/bin/python3
"""
Script that starts a webflask application
"""


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Return Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    return HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    returns C_is_fun
    """
    return "C " + text.replace("_", " ")


@app.route("/python/<text>/", strict_slashes=False)
def python(text="is cool"):
    """
    return Python followed by the value of the text variable
    (replace underscore with a space)
    """
    return "Python " + text.replace("_", " ")


@app.route("/python/", strict_slashes=False)
def python_cool():
    """
    return python is cool
    """
    return "Python is cool"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)