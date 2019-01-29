#Import flask 
from flask import Flask
#Import DateTime
import datetime
#Create an instance of the class
app = Flask(__name__)

@app.route('/date_time')
def date_time():
	return str(datetime.datetime.now())
	

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
	return 'Hello, World'

def hello_world():
        return 'Hello,World!'
if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0', port=8000)


