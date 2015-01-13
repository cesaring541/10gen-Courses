from django.db import models

# Create your models here.


class Author(models.Model):
	author_id = models.AutoField(primary_key=True,blank=False,null=False)
	name = models.CharField(max_length=40)
	email = models.EmailField(blank=False,unique=True)
	password = models.CharField(max_length=50)

	def __unicode__(self):
		return self.email + self.id

class Post(models.Model):
	post_id = models.AutoField(primary_key=True,blank=False,null=False)
	author_id = models.ForeignKey(Author)
	title = models.CharField(max_length=100)
	body = models.TextField()
	publication_date = models.DateField()

	def __unicode__(self):
		return self.title + self.post_id

class Comment(models.Model):
	comment_id = models.ManyToManyField(Post)
	name =  models.CharField(max_length=100)
	email models.EmailField(blank=False)
	comment_text = models.TextField()

	def __unicode__(self):
		return self.email + self.comment_id


class Tag(models.Model)
	tag_id = models.ManyToManyField(Post)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name + self.tag_id



