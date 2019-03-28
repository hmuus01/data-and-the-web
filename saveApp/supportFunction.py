#import wraps which is used will be used in function to check if user is logged in
from functools import wraps
#flask imports
from flask import Flask, render_template, flash,request, redirect, url_for, session, logging,abort
#Function to check if user logged in
def check_user_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return render_template('login.html')
    return wrap


