from flask import Flask
from random import randint

Home = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
High = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
Low = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
Correct = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

random_number = randint(0, 9)

app = Flask(__name__)


@app.route("/")
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            f'<img src={home}>')


@app.route("/<int:number>")
def check(number):
    if number > random_number:
        return ('<h1 style="color:violet">Too high, try again!</h1>'
                f'<img src={High}>')
    elif number < random_number:
        return ('<h1 style="color:red">Too low, try again!</h1>'
                f'<img src={Low}>')
    return ('<h1 style="color:green">Correct Answer</h1>'
            f'<img src={Correct}>')


if __name__ == "__main__":
    app.run(debug=True)
