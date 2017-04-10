import os

class Config(object):
	SECRET_KEY = 'key'

class DevelopmentConfig(Config):
	DEBUG = True