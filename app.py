from flask import Flask, request, render_template, session
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

@app.route('/')
def homepage():
    """Initialize board"""
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    


@app.route('/check-word')
def check_word():
    """Check if word is in dictionary"""

    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    



@app.route('/')