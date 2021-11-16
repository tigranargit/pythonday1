from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #data.db could be any name; sqlite version of sql like mySql, ///mean that it's local, otherwise we can enter password and log in deails etc
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # gets rid of the warning message

db = SQLAlchemy(app)

import application.routes
import application.models