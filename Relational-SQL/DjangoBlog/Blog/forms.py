from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core import validators




class UserForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(),required=True)
	password_confirmation = forms.CharField(widget=forms.PasswordInput(),required=True)

	class Meta:
		model = User
		fields = ('username','email','password','password_confirmation')

	def clean(self):
		password = self.cleaned_data.get('password')
		password_confirmation = self.cleaned_data.get('password_confirmation')

		if password and password != password_confirmation:
			raise forms.ValidationError("Passwords don't match")

		return self.cleaned_data

# class AuthorForm(ModelForm):
# 	class Meta:
# 		model = Author
# 		fields = ('author_id','name','email','password')



class CommentForm(ModelForm):

	name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	comment_text = forms.CharField(widget=forms.Textarea(),required=True)
	class Meta:
		model = Comment
		fields = ('name','email','comment_text')


class PostForm(ModelForm):
	title = forms.CharField(required=True)
	body = forms.CharField(widget=forms.Textarea(),required=True)
	tag_id = forms.CharField(required=True)
	class Meta:
		model = Post
		fields = ('title','body','tag_id')


class TagForm(ModelForm):
	class Meta:
		model = Tag
		fields = ('tag_id','name')

