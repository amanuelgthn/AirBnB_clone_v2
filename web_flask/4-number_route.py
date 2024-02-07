#!/usr/bin/python3
"""
script that starts a webflask application
"""


from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Returns C_is_fun
    """
    return "C " + text.replace("_", " ")


@app.route("/python/(<text>)", strict_slashes=False)
def python(text="is cool"):
    """
    Returns Python is cool
    """
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    returns integers given
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
