from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators


# Article Form Class
class ArticleForm(Form):
    title = StringField('Title', validators = [validators.DataRequired()])
    body = TextAreaField('Body', validators =  [validators.DataRequired()])

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
     ])
    confirm = PasswordField('Confirm Password')

