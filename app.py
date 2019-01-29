from flask import Flask

from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    data = {
        'name': 'Chris Muga',
        'age': 24
    }
    return render_template('index.html', data = data)
@app.route('/login')
def login():
    return 'Login Here...'
@app.route('/profile/<int:id>')
def profile(id):
    return str(id)