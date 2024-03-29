from flask import Flask, render_template
app = Flask(__name__)
@app.route('/hello/')
@app.route('/welcome/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
