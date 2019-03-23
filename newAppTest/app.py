from flask import Flask, render_template, flash,request, redirect, url_for, session, logging,abort
from flask_wtf.csrf import CSRFProtect
#from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask import jsonify

from forms import *

#Flask restful imports
from flask_restful import Api, Resource
from flask_restful import fields, marshal_with
from flask_restful import reqparse

#Initialise app
app = Flask(__name__)

csrf = CSRFProtect(app)
#MySql Confifig
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '04750196'
app.config['MYSQL_DB'] = 'myFlaskapp'
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
                #Create the cursor
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
            # Close connection
            cur.close()

        def post(self, id):
            #Create the cursor
            cur = mysql.connection.cursor()
            # Retrieve articles
            result = cur.execute("SELECT * FROM articles")
            #fetch all articles
            article = cur.fetchall()
            #close the cursor/connection
            cur.close()
            #return
            return article

# API routes
api.add_resource(RetrieveArticlesApi,'/apirestful/<int:id>') 
                
####################################



@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')
################################################################

###############################################################
@app.route('/articles')
def articles():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()

    if result > 0:
        return render_template('articles.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('articles.html', msg=msg)
    # Close connection
    cur.close()
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

#Single Article
@app.route('/article/<string:id>/')
def article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = cur.fetchone()

    return render_template('article.html', article=article) 


#Register a user 
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
             
        #Create cursor
        cur = mysql.connection.cursor()
        
         # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username]) 
        if result > 0:
            flash('USERNAME ALREADY TAKEN','danger')
            return render_template('register.html',form=form) 
        else:      
            # Execute query
            cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
        
            # Commit to DB
            mysql.connection.commit()

            # Close connection
            cur.close()
        
            flash('You are now registered and can log in', 'success')

            return render_template('home.html')
    return render_template('register.html', form=form)


# Login a User
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect('usr/289/dashboard')
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return render_template('login.html')
    return wrap


#logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect("http://www.doc.gold.ac.uk/usr/289/login")

# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    #result = cur.execute("SELECT * FROM articles")
    # Show articles only from the user logged in 
    result = cur.execute("SELECT * FROM articles WHERE author = %s", [session['username']])

    articles = cur.fetchall()

    if result > 0:
        return render_template('dashboard.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('dashboard.html', msg=msg)
    # Close connection
    cur.close()

# Add Article
@app.route('/add_article', methods=['GET', 'POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data
        
        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)",(title, body, session['username']))

        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Article Created', 'success')

        return redirect('http://www.doc.gold.ac.uk/usr/289/dashboard')

    return render_template('add_article.html', form=form)

# Edit Article
@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article by id
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = cur.fetchone()
    cur.close()
    # Get form
    form = ArticleForm(request.form)

    # Populate article form fields
    form.title.data = article['title']
    form.body.data = article['body']
    
    if article['author'] != session ['username']:
        flash('Access Unauthorized','danger')
        return redirect('usr/289/')

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']

        # Create Cursor
        cur = mysql.connection.cursor()
        app.logger.info(title)
        # Execute
        cur.execute ("UPDATE articles SET title=%s, body=%s WHERE id=%s",(title, body, id))
        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Article Updated', 'success')

        return redirect('usr/289/dashboard')

    return render_template('edit_article.html', form=form)



# Delete Article
@app.route('/delete_article/<string:id>', methods=['POST'])
@is_logged_in
def delete_article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Execute
    cur.execute("DELETE FROM articles WHERE id = %s", [id])

    # Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('Article Deleted', 'success')

    return redirect('usr/289/dashboard')


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
    app.run(debug=True, host='0.0.0.0', port=8000)
