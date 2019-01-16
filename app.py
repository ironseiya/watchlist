from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"

@app.route("/index")
@app.route("/home")
def index():
    return "index page"


@app.route("/user/<name>")
def user_name(name='liulin'):
    return "User: %s" % name