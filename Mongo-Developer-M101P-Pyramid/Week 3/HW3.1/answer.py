import pymongo
from pymongo import MongoClient
from bson.son import SON
connection = MongoClient('localhost', 27017)

db = connection.school

students = db.students

item = students.aggregate([
	{ '$unwind' : '$scores' },
	{'$match':{'scores.type':'homework'}},
	{"$group": {"_id": "$_id", "min": {"$min": '$scores.score'}}}
	])
if item:
	for data in item['result']:
		query = {'_id':data['_id']}
		unset = {'$pull':{'scores':{'type':'homework','score':data['min']}}}
		students.update(query,unset)
print "completed remove data"
item = students.aggregate([
	{ '$unwind' : '$scores' },
	{"$group": {"_id": "$_id", "avg": {"$avg": '$scores.score'}}},
	{'$sort':SON([('avg',-1)])},
	])

print item['result'][0]
