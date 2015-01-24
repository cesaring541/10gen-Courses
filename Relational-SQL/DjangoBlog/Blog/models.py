from django.db import models
from django.contrib.auth.models import User

# Create your models here.




# class Author(models.Model):
# 	author_id = models.AutoField(primary_key=True,blank=False,null=False)
# 	name = models.CharField(max_length=40)
# 	email = models.EmailField(blank=False,unique=True)
# 	password = models.CharField(max_length=50)

# 	def __unicode__(self):
# 		return self.email + self.id

# 	class Meta:
# 		db_table = "authors"




class Comment(models.Model):
	comment_id = models.AutoField(primary_key=True,blank=False,null=False)
	name =  models.CharField(max_length=100)
	email = models.EmailField(blank=False)
	comment_text = models.TextField()

	def __unicode__(self):
		return "%s %s" % (self.email,self.comment_id)

	class Meta:
		db_table = "comments"


class Tag(models.Model):
	tag_id = models.AutoField(primary_key=True,blank=False,null=False)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return "%s %s" % (self.name,self.tag_id)

	class Meta:
		db_table = "tags"

class Post(models.Model):
	post_id = models.AutoField(primary_key=True,blank=False,null=False)
	author_id = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	body = models.TextField()
	permalink = models.CharField(default="Not Found",max_length=200)
	publication_date = models.DateTimeField()
	tag_id = models.ManyToManyField(Tag,db_table="post_tags")
	comment_id = models.ManyToManyField(Comment,db_table="post_comments")
	def __unicode__(self):
		return "%s" % self.title

	class Meta:
		db_table = "posts"



