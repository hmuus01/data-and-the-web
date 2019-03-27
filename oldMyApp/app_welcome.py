from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'hamze' or \
                request.form['password'] != 'hmuus001':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return render_template('welcome.html')
    return render_template('login.html', error=error)


@app.route('/search/')
@app.route('/search/<name>')
def hello(name=None):
    return render_template('welcome.html', name=name)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)

