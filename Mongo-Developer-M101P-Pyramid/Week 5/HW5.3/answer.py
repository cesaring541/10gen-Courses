import json,pymongo
from pymongo import MongoClient
db = MongoClient('localhost',27017)
grades = db.test.grades

unwind = {'$unwind':'$scores'}
match = {'$match':{'scores.type':{'$ne':'quiz'}}}
group1 = {'$group':{'_id':{'student_id':'$student_id','class_id':'$class_id'},'avg':{'$avg':'$scores.score'}}}
group2 = {'$group':{'_id':'$_id.class_id','avg':{'$avg':'$avg'}}}
sort = {'$sort':{'avg':-1}}
result = grades.aggregate([unwind,match,group1,group2,sort],cursor={})


if result:
	while result:
		item = result.next()
		print """the class with the best average student performance is %s""" % item['_id']
		break
