from application import app, db
from application.models import Rounds
from flask import redirect, url_for
from random import choice

@app.route('/') #you can specify request type my isting methods = ['GET'] for example
def home(): 
    results = Rounds.query.all()
    return '\n'.join([f"Player played {result.player_move}, computer played {result.comp_move}. {result.winner} wins!" for result in results])

@app.route('/play-<move>')
def play(move):
    winning_moves = {'rock':'paper','paper': 'scissors', 'scissors':'rock' }
    comp_move = choice(['rock', 'paper','scissors'])
    if move == winning_moves[comp_move]: #here we refer to keys and values in the dictionaries, each key has a corresponding value that "beats" the key
        winner = 'Player'
    elif move ==comp_move:
        winner = 'None'
    else:
        winner = 'Computer'
    
    newres = Rounds(player_move=move, comp_move = comp_move, winner = winner)
    db.session.add(newres)
    db.session.commit()
    return redirect(url_for('home'))