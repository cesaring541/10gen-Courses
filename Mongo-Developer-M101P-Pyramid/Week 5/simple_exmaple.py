import pymongo
from pymongo import MongoClient

mongo  = MongoClient('mongodb://localhost:27017')
db = mongo.agg.products

data = db.aggregate([
	{
	"$group":{
		"_id":"$manufacturer",
		"num_products":{"$sum":1}
		}
	}
])

print data
