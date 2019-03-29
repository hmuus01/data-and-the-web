from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators



# Article Form Class
class ArticleForm(Form):
    title = StringField('Title', validators = [validators.DataRequired()])
    body = TextAreaField('Body', validators =  [validators.DataRequired()])

#Register form class
class RegisterForm(Form):
    #name field where the user enters their name, set the minimum to 1 characher and a max of 50   
    name = StringField('Name', [validators.Length(min=1, max=50)])
    #username also uses stringField witch a set minimum of 4 characters and max of 30
    username = StringField('Username', [validators.Length(min=4, max=30)])
    #email also uses stringField with a set minimum of 5 charachters and maximum of 55
    email = StringField('Email', [validators.Length(min=5, max=55)])
    #password field with a couple validators one is the dataRequired and the other for the validators.EqualTo which will be equal toa field called confirm.
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
     ])
    #A confirm field which is equal to a password field with the label "Confirm password"  
    confirm = PasswordField('Confirm Password')

