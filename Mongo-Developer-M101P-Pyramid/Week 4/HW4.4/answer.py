import sys, pymongo
from pymongo import MongoClient
from bson.son import SON
import re
connection = MongoClient('localhost', 27017)

db = connection.m101
profile = db.profile
_reg = re.compile('school2')
items = profile.find({'ns':_reg}).sort([('millis',-1)])
for i in items:
	print 'The latency of the longest running operation to the collection %s ms' % i['millis']
	break
