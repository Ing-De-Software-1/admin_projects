# -*- coding: utf-8 -*-

from flask_mail import Mail, Message

from views import app
from keys import *


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = username
app.config['MAIL_PASSWORD'] = password
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = 'Mail from Flask: \t'
app.config['FLASKY_MAIL_SENDER'] = 'This is a Flask test <flasky@example.com>'
app.config['FLASKY_ADMIN'] = the_admin

mail = Mail(app)


def send_email(to, subject, message):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + '' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = "Hello"
    msg.html = message
    mail.send(msg)