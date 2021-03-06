#!/usr/bin/env python
# coding=utf-8
# coding: utf8
from wtforms import Form, StringField, PasswordField, validators, TextAreaField, SelectField,IntegerField,FileField
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

    password2= PasswordField('Password Confirm',
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
    carrera= StringField('Degree',
                          [
                              validators.Required(message='Obligatorio'),
                              validators.length(min=4, max=25, message='Carrera invalida,'
                                                                       'minimo 4 caracteres, maximo 25')
                          ])

    semestre = SelectField('Semestre', choices=[('1', '1'), ('2', '2'),('3', '3'),
                                                ('4', '4'), ('5', '5'), ('6', '6'),
                                                ('7', '7'), ('8', '8'), ('9','9')])
    cuenta = StringField('Numero De Cuenta',
                          [
                              validators.Required(message='Obligatorio'),
                              validators.length(min=9, max=10, message='Número de cuenta incorrecto,'
                                                                       'minimo 9 caracteres, maximo 10')
                          ])

class EquipoForm(Form):
    name= StringField('Nombre del Equipo',
                      [
                          validators.Required(message='Obligatorio'),
                          validators.length(min=4, max=25, message='Nombre invalido,'
                                                                   'minimo 3 caracteres, maximo 25')
                      ])
"""
    logo = FileField('Logo')
    account = SelectField('MembersNumbers', choices=[('1', '1'), ('2', '2'),('3', '3'),
                                                    ('4', '4'), ('5', '5'), ('6', '6'),
                                                    ('7', '7'), ('8', '8'), ('9','9')])
    #nombre, #integrantes, logo, proyecto, horario, alumnos
"""

class ProyectoForm(Form):
    name= StringField('Nombre del Proyecto',
                      [
                          validators.Required(message='Obligatorio'),
                          validators.length(min=4, max=25, message='Nombre invalido,'
                                                                   'minimo 4 caracteres, maximo 25')
                      ])
    descripcion = TextAreaField('Describe tu proyecto',
                         [
                             validators.Required(message='Obligatorio'),
                         ])

    #nombre,descripcion,duracion,equipo