from flask import Flask, request, render_template
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"



