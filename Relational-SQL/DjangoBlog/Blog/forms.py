from .models import *
from django.forms import ModelForm

class AuthorForm(ModelForm):
	class Meta:
		model = Author
		fields = ('author_id','name','email','password')



class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('comment_id','name','email','comment_text')


class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ('post_id','title','body','publication_date')


class TagForm(ModelForm):
	class Meta:
		model = Tag
		fields = ('tag_id','name')

