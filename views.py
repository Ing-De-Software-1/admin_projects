from flask import Flask, render_template,request, session, redirect, url_for,flash
from config import DevelopmentConfig
from models import *
app = Flask(__name__)
app.config.from_object('config')
app.config.from_object(DevelopmentConfig)

   
@app.errorhandler(404)
def not_found(error):
	return "Not Found."

@app.errorhandler(500)
def server_error(e):
    return 'An internal error occurred.', 500

@app.route(r'/', methods=['GET','POST'])
def index():
	#return render_template('index.html')
    user = User(username='GDG')
    user.put()
    userr = User(username='UNAM')
    userr.put()
    a = str(user)
    return render_template('index.html',a=a)