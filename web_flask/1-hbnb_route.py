#!/usr/bin/python3
"""Start Flask web app
The app listens on 0.0.0.0, port 5000.
Routes:
    /: Display'Hello HBNB!'.
    /hbnb: Display 'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display'HBNB'."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
