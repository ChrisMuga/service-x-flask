from flask import Flask, jsonify

from flask import render_template
from flask_sqlalchemy import SQLAlchemy

import logging
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:root@localhost/servicex'
db = SQLAlchemy(app)

class Users(db.Model):

        id              = db.Column(db.Integer, primary_key=True)
        first_name      = db.Column(db.String(250), unique=True, nullable=False)
        last_name       = db.Column(db.String(250), unique=True, nullable=False)
        email_address   = db.Column(db.String(250), unique=True, nullable=False)


        def __repr__(self):
            return '<User %r>' % self.email_address

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

@app.route('/connect')
def connect():
    
    users = Users(
                    id              =   '1253456', 
                    first_name      =   'Tony', 
                    last_name       =   'Momtana', 
                    email_address   =   'tony@mail.com' 
                )
    db.session.add(users)
    db.session.commit()
    return 'DB'

@app.route('/fetch')
def fetch():
    x = Users.query.all()

    #logging
    logging.info('done')
    return len(str(x))

    
    
    
    


    
