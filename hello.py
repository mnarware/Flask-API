from flask import Flask
import pandas as pd

app=Flask(__name__)
@app.route("/")
def hello():
     return "Hey Congrats, you successfully created sample Flask app"
     print(pd.__version__)
@app.route("/ping")
def anything():
     return "Why are ypu pinging me."