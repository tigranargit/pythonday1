from flask import Flask, redirect, url_for

app = Flask(__name__) #python virable, has to be (__name__)

@app.route('/<aname>')
def home(aname):
#   return redirect(f'/hello {name}') redirect function 
    return redirect(url_for('hello', name=aname)) #redirect function with url_for

@app.route('/hello/<name>')
def hello(name):
    return f"Hello {name}!"

app.run(debug=True)
