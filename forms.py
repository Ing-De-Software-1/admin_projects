#!/usr/bin/env python
# coding=utf-8
# coding: utf8
from wtforms import Form, StringField, PasswordField, validators, TextAreaField, SelectField
from wtforms.fields.html5 import EmailField


class LoginForm(Form):
    username= StringField('Username',
                          [
                              validators.Required(message='Obligatorio'),
                              validators.length(min=4, max=25, message='Nombre invalido,'
                                                                       'minimo 4 caracteres, maximo 25')
                          ])

    password= PasswordField('Password',
                            [
                                validators.Required(message='Obligatorio'),
                                validators.length(min=4, max=25, message='Password invalido,'
                                                                         'minimo 4 caracteres, maximo 25')
                            ])

class RegisterForm(Form):
    username= StringField('Username',
                          [
                              validators.Required(message='Obligatorio'),
                              validators.length(min=4, max=25, message='Nombre invalido,'
                                                                       'minimo 4 caracteres, maximo 25')
                          ])

    password= PasswordField('Password',
                            [
                                validators.Required(message='Obligatorio'),
                                validators.length(min=4, max=25, message='Password invalido,'
                                                                         'minimo 4 caracteres, maximo 25')
                            ])

    email= EmailField('Email',
                      [
                          validators.Required(message='Obligatorio'),
                          validators.Email(message='E-mail invalido')
                      ])