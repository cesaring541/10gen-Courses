import re,pymongo
from pymongo import MongoClient
db = MongoClient('localhost',27017)
zips = db.test.zips


city = re.compile('[0-9]')
project = {'$project':{ 'city_without_digit': {'$substr' : ["$city",0,1]},'pop':1}}
match = {'$match':{'city_without_digit':city}}
group = {'$group':{'_id':'null','total':{'$sum':'$pop'}}}
result = zips.aggregate([project,match,group],cursor={})

if result:
	while result:
		item = result.next()
		print """sum total of people who are living in a zip code
			where the city starts with a digit is %s""" % item['total']
		break
