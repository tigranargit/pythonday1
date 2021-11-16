from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__) #python virable, has to be (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # 'mysql+pymsql://<user>:<password>@<ip address>:3306/<database name>' you don't have angle brackets in actual uri name
app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.string(50))
    def __repr__(self): #__repr__ method will be called and only shame the name 
        return self.name

@app.route('/<aname>')
def home(aname):
    users = Users.query.all()
#   return redirect(f'/hello {name}') redirect function 
#   return redirect(url_for('hello', name=aname)) #redirect function with url_for
#    return users
    return str([user.name for user in users]) #shows your user table in a nice way, only names 


@app.route('/add/<name>')
def add(name):
    user = Users(name=name)
    db.session.add(user)
    db.session.commit()

app.run(debug=True)