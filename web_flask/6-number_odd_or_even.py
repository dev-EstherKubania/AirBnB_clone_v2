#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!" when the root URL is accessed.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB" when /hbnb is accessed.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Display "C " followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """
    Display "Python " followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    The default value of text is "is cool".
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Display "n is a number" only if n is an integer.
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Display an HTML page with an H1 tag: "Number: n" if n is an integer.
    """
    return render_template('6-number_template.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Display an HTML page with an H1 tag: "Number: n is even|odd" if n is an integer.
    """
    return render_template('6-number_odd_or_even.html', n=n, odd_even="odd" if n % 2 != 0 else "even")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
