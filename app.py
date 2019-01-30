from flask import Flask, jsonify

from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, DBAPIError, OperationalError, InternalError
# marshmallow for serializing sqlalchemy data
from flask_marshmallow import Marshmallow

import logging
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:root@localhost/servicex'
db = SQLAlchemy(app)

# marshmallow after sql-alchemy
ma = Marshmallow(app)

#create sql-alchemy model.
class Users(db.Model):

        id              = db.Column(db.Integer, primary_key=True)
        first_name      = db.Column(db.String(250), unique=True, nullable=False)
        last_name       = db.Column(db.String(250), unique=True, nullable=False)
        email_address   = db.Column(db.String(250), unique=True, nullable=False)


        def __repr__(self):
            return {
                'email_address': self.email_address
            }


#create marshmallow schema (from sqlalchemy model)
class UsersSchema(ma.ModelSchema):
    class Meta:
        model = Users

#instantiate schemas

#single record [one]
user     = UsersSchema(strict = True)

#multiple records [many]
users    = UsersSchema(many=True, strict = True)

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
    try:
        users = Users(
                        id              =   '1253456', 
                        first_name      =   'Tony', 
                        last_name       =   'Momtana', 
                        email_address   =   'tony@mail.com' 
                    )
        db.session.add(users)
        db.session.commit()
        return 'DB'
    except IntegrityError:

        response =  {
                        'code'  :   0,
                        'msg'   :   'Integrity Error'
                    }

    except DBAPIError:

        response =  {
                        'code'  :   0,
                        'msg'   :   'DBAPIError'
                    }

    except OperationalError:

        response =  {
                        'code'  :   0,
                        'msg'   :   'OperationalError'
                    }

    except InternalError:

        response =  {
                        'code'  :   0,
                        'msg'   :   'InternalError'
                    }
    finally:

        return jsonify(response)

    

@app.route('/fetch')
def fetch():

    #fetch all users
    x = Users.query.all()

    #parse dataset into an object [marshmallow]
    result = users.dump(x)

    #parse to json string
    data = jsonify(result.data)
    
    #return values
    return data



    
    
    
    


    
