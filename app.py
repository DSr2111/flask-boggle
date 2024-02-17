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

    


@app.route('/')



@app.route('/')