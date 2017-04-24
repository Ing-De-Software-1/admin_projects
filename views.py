from flask import Flask, render_template,request, session, redirect, url_for,flash
from config import DevelopmentConfig
from models import *
import forms

app = Flask(__name__)
app.config.from_object('config')
app.config.from_object(DevelopmentConfig)

   
@app.errorhandler(404)
def not_found(error):
	return "Not Found."

@app.errorhandler(500)
def server_error(e):
    return 'An internal error occurred.', 500

@app.route(r'/')
def index():
	return render_template('index.html')

@app.route(r'/login', methods=['GET','POST'])
def login():
    form_log = forms.LoginForm(request.form)
    form_reg = forms.RegisterForm(request.form)
    e = ""
    if request.method== 'POST' and form_log.validate():
        user= form_log.username.data
        password= form_log.password.data
        return redirect(url_for('home'))
    return render_template('login.html', login=form_log , registro=form_reg, e=e)


@app.route(r'/home', methods=['GET'])
def home():
    return render_template('home.html')


@app.route(r'/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('index'))
