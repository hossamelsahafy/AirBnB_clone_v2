#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello Function"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function To Display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """Function To Display Text After C"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Function To Display Text After Python"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    if n.isdigit():
        return "{} is a number".format(n)
    else:
        return "Not Found", 404


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """Function That Render Template"""
    if n.isdigit():
        return render_template('5-number.html', n=n)
    else:
        return "Not Found", 404


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def number_odd_or_even(n):
    """Function To Define The Integer As Even Or Odd"""
    if n.isdigit():
        n = int(n)
        if n % 2 == 0:
            return render_template(
                '6-number_odd_or_even.html', n=n, parity='even')
        elif n % 2 != 0:
            return render_template(
                '6-number_odd_or_even.html', n=n, parity='odd')
    else:
        return "Not Found", 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)