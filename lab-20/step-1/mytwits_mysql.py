from flask import Flask, request
from flask import render_template
from flask import redirect, url_for
from flask import flash
from vs_url_for import vs_url_for
from forms import loginForm
from dbhelper import DBHelper
from flask_login import LoginManager, login_required
from flask_login import login_user, logout_user
from flask_login import current_user
from user import User
login_manager = LoginManager()
from dbhelper import db
from twits_blueprint import twits_blueprint

app = Flask(__name__)
login_manager.init_app(app)
app.register_blueprint(twits_blueprint)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#---- the callback function for flask-login
@login_manager.user_loader
def load_user(user_id):
    result = db.get_user(user_id)
    if result: 
        username = result[1]
        return User(user_id,username)

   
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        password = form.password.data
        username = form.username.data
        user_id = db.check_password(username,password)
        if user_id:
            user = User(user_id, username)
            login_user(user)
            return redirect(vs_url_for('twits_blueprint.index'))
        else:
            flash('login unsuccessful!')
    return render_template('login.html',form=form)

      
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    logout_user()
    return redirect(vs_url_for('twits_blueprint.index'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
