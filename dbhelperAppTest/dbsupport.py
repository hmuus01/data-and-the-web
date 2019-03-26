#import mysql for the database
from flask import Flask, render_template, flash,request, redirect, url_for, session, logging,abort
from flask_mysqldb import MySQL

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



