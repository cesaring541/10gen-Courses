from mongoengine import *
import datetime


class User(Document):
	username = StringField(max_length=200,required=True)
	password = StringField(max_length=200,required=True)


class Post(Document):
	title = StringField(max_length=200,required=True)
	author = ReferenceField(User)
	body = StringField(required=True)
	permalink = StringField()
	tags = ListField()
	comments = ListField()
	date = DateTimeField()

class Session(Document):
	username = ReferenceField(User)
