from flask import Flask
import random

app = Flask(__name__)

print(__name__)
print(random.__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! hello</p>"


@app.route("/bye")
def bye_bye():
    return "<p>Bye Bye, World!</p>"


if __name__ == "__main__":
    app.run()
