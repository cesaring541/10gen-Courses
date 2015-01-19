from django.shortcuts import render,render_to_response,redirect
from django.views.generic import ListView,DetailView
from django.contrib.auth import logout
from .models import *
# Create your views here.


class Index(DetailView):

	def get(self,request):
		return render_to_response('welcome.tpl')


class SignUpView(DetailView):
	def get(self,request):
		return render_to_response('users/signup.tpl')

class LoginView(DetailView):
	def get(self,request):
		import ipdb; ipdb.set_trace()
		return render_to_response('users/login.tpl')

class LogOutView(DetailView):
	def get(self,request):
		if request.user.is_authenticated():
			logout(request)
		return redirect('/')
