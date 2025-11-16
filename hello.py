from flask import Flask

app=Flask(__name__)
@app.route("/")
def hello():
     return "Hey Congrats, you successfully created sample Flask app"

@app.route("/ping")
def anything():
     return "Why are ypu pinging me."