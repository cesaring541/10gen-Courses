import mongoengine
from mongoengine import connect

CONN = None

MONGO = {
'DB':'blog',
'USERNAME':'admin',
'PASSWORD':'admin',
'HOST':'localhost',
'PORT':'27017'
}

def includeme(config):
	try:
		config.db
	except AttributeError:
		config.db = None
	config.db = connect(MONGO['DB'])
