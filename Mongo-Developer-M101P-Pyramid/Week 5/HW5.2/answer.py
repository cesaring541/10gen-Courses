import json,pymongo
from pymongo import MongoClient
db = MongoClient('localhost',27017)
zips = db.agg.zips


match = {'$match':{'_id.state':{'$in':['CA','NY']},'sum':{'$gt':25000}}}
group1 = {'$group':{'_id':{'state':'$state','city':'$city'},'sum':{'$sum':'$pop'}}}
group2 = {'$group':{'_id':'null','avg':{'$avg':'$sum'}}}

result = zips.aggregate([group1,match,group2],cursor={})
if result:
	while result:
		item = result.next()
		print """Resut the average population of cities in California
			and New York with populations over 25,000 is %d""" % round(item['avg'])
		break
