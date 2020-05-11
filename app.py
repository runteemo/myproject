from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>hello world!</h1>'


@app.route('/greet', defaults={'name': 'teemo'})
@app.route('/greet/<name>')
def index(name):
    return '<h1>hello.%s!</h1>' % name
