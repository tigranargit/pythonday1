#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#import random

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #data.db could be any name; sqlite version of sql like mySql, ///mean that it's local, otherwise we can enter password and log in deails etc
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # gets rid of the warning message

#@app.route('/play')

#def my_turn():
 #   figure_list = ['rock', 'scissors','paper']
  #  my_figure_index = random.randrange(len(figure_list))
   # cpu_figure_index = random.randrange(len(figure_list))
    #my_figure = figure_list[my_figure_index]
    #cpu_figure = figure_list[cpu_figure_index]
    
   # if my_figure == cpu_figure
    
    #return f"Your figure is: {my_figure} Computer figure is: {cpu_figure}"
    

#app.run(debug=True)