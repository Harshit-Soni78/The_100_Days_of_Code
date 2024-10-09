from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World! hello</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200px>')


@app.route("/bye")
def bye():
    return "Bye"


@app.route("/<name>/<int:number>")
def great(name, number):
    return f"Hello {name}, you are {number} year old!"


if __name__ == "__main__":
    app.run(debug=True)
