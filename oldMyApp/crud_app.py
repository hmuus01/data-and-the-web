from flask import Flask, flash, redirect, render_template, \
     request, url_for, session , redirect
from flask.ext.pymongo import Pymongo
import bcrypt

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in'
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'hamze' or request.form['password'] != 'hmuus001':
            error = 'Inval'
            flash('ERROR!!')
        else:
            flash('You were successfully logged in')
            return render_template('welcome.html')
    return render_template('login.html', error=error)

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user =  users.find_one({'name': request.form['username']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw[request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'],' password' : hashpass})
            session['username'] = request.form['username']
            return redirect(ur_for('index')) 
        return 'That username already exists!'

@app.route('/search/')
@app.route('/search/<name>')
def hello(name=None):
    return render_template('welcome.html', name=name)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
