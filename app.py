from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route("/home")
@app.route("/index")
def hello_world():
    return 'Hello world'
    