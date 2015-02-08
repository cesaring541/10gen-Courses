import json,pymongo
from pymongo import MongoClient

db = MongoClient('localhost',27017)
posts = db.blog.posts

unwind = {'$unwind':'$comments'}
group = {'$group':{'_id':'$comments.author','total':{'$sum':1}}}
sort = {'$sort':{'total':-1}}

result = posts.aggregate([unwind,group,sort],cursor={})
if result:
	while result:
		item = result.next()
		print 'The author with the greatest number of comments is %s' % item['_id']
		break
