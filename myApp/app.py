#flask imports
from flask import Flask, render_template, flash,request, redirect, url_for, session, logging,abort
#import csrf for protection for my app
from flask_wtf.csrf import CSRFProtect
#import mysql for the database
from flask_mysqldb import MySQL
#import sql_ alchemy
from flask_sqlalchemy import SQLAlchemy
#import wtf-forms for the registration and login forms
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
#import passlib.hash for protection of user passwords which hash's and uses salt
from passlib.hash import sha256_crypt
#import wraps which is used will be used in function to check if user is logged in
from functools import wraps
#import jsonify for the api
from flask import jsonify
#import the form classes from forms.py
from forms import *

from supportFunction import *
#Flask restful imports
from flask_restful import Api, Resource
from flask_restful import fields, marshal_with
from flask_restful import reqparse

#Create Instance of Flask class/ place holder for the current module
app = Flask(__name__)

#wrap the app with csrf protection
csrf = CSRFProtect(app)
#MySql Configurations

#Name of host to connect to
app.config['MYSQL_HOST'] = 'localhost'
#User to authenticate as which is set to root
app.config['MYSQL_USER'] = 'root'
#password to authenticate with
app.config['MYSQL_PASSWORD'] = '04750196'
#database to use
app.config['MYSQL_DB'] = 'myFlaskapp'
#Cursor class
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#Initalise MYSQL
mysql = MySQL(app)

api = Api(app)

#Initialise Resource Fields
resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'author': fields.String,
    'body': fields.String,
    'date': fields.DateTime(dt_format='rfc822')
}

#Request Parser for the api
parser = reqparse.RequestParser()
parser.add_argument('id',type=int,help='id of article; must be an integer')
parser.add_argument('title', type=str, help='name of article; a string')
parser.add_argument('author', type=str, help='name of author; must be string')
parser.add_argument('body', type=str, help='body of text, must be a string')

#Retrieve articles using Api class
class RetrieveArticlesApi(Resource):
        #output filter decorator
        @marshal_with(resource_fields)
        def get(self,id):
                #Create the cursor which operates as a handler to handle queries
                cur = mysql.connection.cursor()
                #retrieve articles
                result = cur.execute("SELECT * FROM articles WHERE id=%s", [id])
                #fetch article
                article = cur.fetchone()
                #close the cursor/connection
                cur.close()
                #Return
                return article

        #output filter decorator
        @marshal_with(resource_fields)
        def delete(self,id):
            #Create the cursor
            cur = mysql.connection.cursor()
            # Execute deletion of articles
            result = cur.execute("DELETE FROM articles WHERE id=%s", [id])
            # Commit DB
            mysql.connection.commit()
            result = cur.execute("SELECT * FROM articles")
            article = cur.fetchall()
            # Close connection
            cur.close()
            return articles
            
        
        def put(self, id):
            args = parser.parse_args()
            main = args['body']
            # Create Cursor which operates as a handler and handles queries
            cur = mysql.connection.cursor()
            # Execute
            test = "API Edit"
            cur.execute ("UPDATE articles SET title=%s, body=%s WHERE id=%s",(test,main,id))
            # Commit to DB
            mysql.connection.commit()
            #close the cursor/connection
            cur.close()
            #return
            return

# Restful API route
api.add_resource(RetrieveArticlesApi,'/apirestful/<int:id>') 
#Route for the homepage
@app.route('/')
def home():
    return render_template('home.html')

#Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

#route for the forum/articles for all users
@app.route('/articles')
def articles():
    # Create cursor which operates as a handler and handles queries
    cur = mysql.connection.cursor()

    # Get all articles
    result = cur.execute("SELECT * FROM articles")
    #fetch all articles
    articles = cur.fetchall()
    #check if there are any articles if there are not print message to the user to let them know
    if result > 0:
        return render_template('articles.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('articles.html', msg=msg)
    # Close connection
    cur.close()

#route to find Boxing Gyms
@app.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        destination = request.form['destination']
        return redirect('usr/289/find/'+str(destination))
    return render_template('find.html')

#Find Gym
@app.route('/find/<name>', methods=['GET', 'POST'])
def findgym(name=None):
    if request.method == 'POST':
        destination = request.form['destination']
        return redirect('usr/289/find/'+str(destination))
    return render_template('find.html', name=name)

#Single Article app route
@app.route('/article/<string:id>/')
def article(id):
    # Create cursor which operates as a handler and handles queries
    cur = mysql.connection.cursor()

    # Get article by article
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    #fetch one article
    article = cur.fetchone()
    #render the article html page
    return render_template('article.html', article=article) 


#Register a user 
@app.route('/register', methods=['GET', 'POST'])
def register():
    #Form variable which is set to the RegisterForm which was created in the class RegisterForm
    form = RegisterForm(request.form)
    #Check if the request to the route is POST and the form data validates 
    if request.method == 'POST' and form.validate():
        #store the form name submitted to the variable name
        name = form.name.data
        #store the form submitted in the email field in the variable email
        email = form.email.data
        #store the username the user creats in the username variable
        username = form.username.data
        #Hash and salt the password the user enters and store in the password variable
        password = sha256_crypt.encrypt(str(form.password.data))
             
        #Create cursor which operates as a handler and handles queries
        cur = mysql.connection.cursor()
        
         # Get the  user by username and store in result
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username]) 
        #check if the username is taken
        if result > 0:
            #if the username is taken let the user know
            flash('USERNAME ALREADY TAKEN','danger')
            #redirect the user to the register page
            return render_template('register.html',form=form) 
        else:      
            # Execute query to store the registration in the database
            cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
        
            # Commit to the database
            mysql.connection.commit()

            # Close connection
            cur.close()
            #flash meessage to let the user know they've been registered
            flash('You are now registered and can log in', 'success')
            #redirect the user to the homepage
            return render_template('home.html')
    return render_template('register.html', form=form)


# Login a User
@app.route('/login', methods=['GET', 'POST'])
def login():
    #check if the request to the route is a POST method
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor which operates as a handler and handles queries
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
        #check if the username exits
        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare the Passwords, the password the user enters in the form and the stored password
            if sha256_crypt.verify(password_candidate, password):
                # if the passwords are the same, start session
                session['logged_in'] = True
                session['username'] = username
                #Notify the user they are logged in
                flash('You are now logged in', 'success')
                return redirect('usr/289/dashboard')
            else:
                #else let the user know they entered incorrect details
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

#Function to check if user logged in


#logout app route
@app.route('/logout')
#only show if user is logged in
@check_user_logged_in
def logout():
    #on logout clear the session
    session.clear()
    #notify the user they are now logged out
    flash('You are now logged out', 'success')
    #redirect the user to the login page
    return redirect("http://www.doc.gold.ac.uk/usr/289/login")

# Dashboard app route
@app.route('/dashboard')
#only show if user is logged in
@check_user_logged_in
def dashboard():
    # Create cursor which operates as a handler and handles queries
    cur = mysql.connection.cursor()

    # Get articles
    #result = cur.execute("SELECT * FROM articles")
    # Show articles only from the user logged in 
    result = cur.execute("SELECT * FROM articles WHERE author = %s", [session['username']])
    #get all articles
    articles = cur.fetchall()
    #if there are articles found redirect the user to the dashboard page 
    if result > 0:
        return render_template('dashboard.html', articles=articles)
    else:
        #else notify the user there are no articles
        msg = 'No Articles Found'
        return render_template('dashboard.html', msg=msg)
    # Close connection
    cur.close()

# Add Article
@app.route('/add_article', methods=['GET', 'POST'])
@check_user_logged_in
def add_article():
    form = ArticleForm(request.form)
    #Check if the request to the route is POST and the form data validates
    if request.method == 'POST' and form.validate():
        #if so, store the information submitted in the title and body variables
        title = form.title.data
        body = form.body.data
        
        # Create Cursor which operates as a handler and handles queries
        cur = mysql.connection.cursor()

        # Execute sql command adding an article to the database under the logged in user's name
        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)",(title, body, session['username']))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()
        #notify the user an article has been created
        flash('Article Created', 'success')
        #redirect the user to the dashboard
        return redirect('http://www.doc.gold.ac.uk/usr/289/dashboard')
    return render_template('add_article.html', form=form)

# Edit Article
@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
@check_user_logged_in
def edit_article(id):
    # Create cursor which operates as a handler and handles queries
    cur = mysql.connection.cursor()

    # Get article by id
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    #retrive one article
    article = cur.fetchone()
    #close the connection
    cur.close()
    # Get form
    form = ArticleForm(request.form)
    # Populate article form fields
    form.title.data = article['title']
    form.body.data = article['body']
    #if the author is not the user logged in then do not give them access to edit the article
    if article['author'] != session ['username']:
        flash('Access Unauthorized','danger')
        #redirect the user to the homepage
        return redirect('usr/289/')
    #Check if the request to the route is POST and the form data validates
    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']

        # Create Cursor which operates as a handler and handles queries
        cur = mysql.connection.cursor()
        app.logger.info(title)
        # Execute
        cur.execute ("UPDATE articles SET title=%s, body=%s WHERE id=%s",(title, body, id))
        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()
        #notify the user the article was updated
        flash('Article Updated', 'success')
        #redirect the user to the dashboard
        return redirect('usr/289/dashboard')

    return render_template('edit_article.html', form=form)



# Delete Article
@app.route('/delete_article/<string:id>', methods=['POST'])
@check_user_logged_in
def delete_article(id):
    # Create cursor which operates as a handler and handles queries
    cur = mysql.connection.cursor()

    # Execute
    cur.execute("DELETE FROM articles WHERE id = %s", [id])

    # Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()
    #let the user know that an article was deleted
    flash('Article Deleted', 'success')

    return redirect('usr/289/dashboard')

#route for the api
@app.route('/api')
@app.route('/api/<author>')
def api(author=None):
    if author:
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM articles WHERE author = %s", [author])
        articles = cur.fetchall()
        cur.close()
        return jsonify({'Reviews':articles})
    else:
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM articles")
        articles = cur.fetchall()
        cur.close()
        return jsonify({'Reviews':articles})

if __name__ == '__main__':
    app.secret_key ='secret123'
    app.WTF_CSRF_SECRET_KEY = 'secret1122'
    app.run(debug=False, host='0.0.0.0', port=8000)
