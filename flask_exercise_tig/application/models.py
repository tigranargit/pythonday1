from application import db

class Rounds(db.Model): #db.Model where Mode is what we have to type to create a table; db is the name of the table we have given in __init__.py
    rid = db.Column(db.Integer, primary_key = True)
    player_move = db.Column(db.String(10))
    comp_move = db.Column(db.String(10))
    winner = db.Column(db.String(10))