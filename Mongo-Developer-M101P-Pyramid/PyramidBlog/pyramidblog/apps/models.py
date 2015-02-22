from mongoengine import *
import datetime


class User(Document):
	_id = StringField(primary_key=True)
	password = StringField(max_length=200,required=True)
	email = EmailField()
	meta = {'collection': 'users'}

class Post(Document):
	title = StringField(max_length=200,required=True)
	author = ReferenceField(User)
	body = StringField(required=True)
	permalink = StringField()
	tags = ListField()
	comments = ListField()
	date = DateTimeField()
	meta = {'collection': 'posts'}

class Session(Document):
	username = ReferenceField(User)
	meta = {'collection': 'sessions'}
