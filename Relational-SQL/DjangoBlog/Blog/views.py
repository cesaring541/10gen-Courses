from django.shortcuts import render,render_to_response,redirect
from django.views.generic import ListView,DetailView
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import *
from .models import *
# Create your views here.


class Index(DetailView):
	def get(self,request):
		return render(request,'welcome.tpl')

class Blog(DetailView):
	def get(self,request):
		render(request,'blog_template.tpl')

class SignUpView(DetailView):
	def get(self,request):
		form = UserForm()
		return render(request,'users/signup.tpl',{'form':form})

	def post(sefl,request):
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
		return render(request,'users/signup.tpl',{'form':form})


class LoginView(DetailView):
	def get(self,request):
		print request.user
		error = None
		if 'error' in request.session:
			print request.session['error']
			error = request.session['error']
			del request.session['error']
		return render(request,'users/login.tpl',{'error':error})

	def post(self,request):
		error = None
		email = request.POST['username']
		password = request.POST['password']
		try:
			_U = User.objects.get(email=email)
			user = authenticate(username=_U.username, password=password)
			if user:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect(reverse('index'))
				else:
					request.session['error'] = "Sorry your account is disabled"
			else:
				request.session['error'] = "Password inccorect"
		except User.DoesNotExist:
				request.session['error'] = "Email does not exists"
		return HttpResponseRedirect(reverse('login'))

class LogOutView(DetailView):
	def get(self,request,next='/'):
			if request.user.is_authenticated():
				logout(request)
			return redirect(next)
