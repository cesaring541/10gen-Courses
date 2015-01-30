import sys,os
import pymongo
from pymongo import MongoClient
from bson.son import SON
import subprocess
connection = MongoClient('localhost', 27017)

db = connection.blog
posts = db.posts
posts.create_index([('date',pymongo.DESCENDING)])
posts.create_index([('tags',pymongo.ASCENDING),('date',pymongo.DESCENDING)])
posts.create_index('tags')
posts.create_index('permalink')

subprocess.check_call(["python", "hw4-3/validate.py"])
