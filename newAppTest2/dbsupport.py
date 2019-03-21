import pymysql
import datetime
import hashlib

#MySql Confifig
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '04750196'
app.config['MYSQL_DB'] = 'myFlaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

def __init__(self):
    self.db = pymysql.connect(host = 'localhost',
    user = 'root',
    password = '04750196',
    db = 'myFlaskapp')

