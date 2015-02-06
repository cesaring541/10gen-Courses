import json,pymongo
from pymongo import MongoClient
import pprint
mongo  = MongoClient('mongodb://localhost:27017')
db = mongo.agg.products

with open('data.json','r') as json_data:
	_datas = json.load(json_data)
	for _item in _datas:
		print "insert data " + str(_item) + " into products collection"
		db.insert(_item)

