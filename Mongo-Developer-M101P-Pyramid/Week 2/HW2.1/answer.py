import pymongo
from pymongo import MongoClient
import sys
import json
try:
	connection = MongoClient('localhost', 27017)
	db = connection.students
	grades = db.grades
	_query = {'type':'exam','score':{'$gte':65}}
	_datas = grades.find(_query).sort('score',pymongo.ASCENDING).limit(1)
	for _data in _datas:
		print _data
except:
	print sys.exc_info()
