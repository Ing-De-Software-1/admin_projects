import os

class Config(object):
	SECRET_KEY = 'admin-key'

class DevelopmentConfig(Config):
	DEBUG = True