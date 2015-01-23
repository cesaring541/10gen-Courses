from django.shortcuts import render,render_to_response,redirect
from django.views.generic import ListView,DetailView
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *
from .models import *
import datetime
# Create your views here.


class IndexView(DetailView):
	def get(self,request):
		context_dict = {}
		_posts = Post.objects.all()[:10]
		context_dict['posts'] = _posts
		return render(request,'index.tpl',context_dict)

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
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save()
			return HttpResponseRedirect(reverse('login'))
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
					return HttpResponseRedirect(reverse('welcome'))
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


class WelComeView(DetailView):
	@method_decorator(login_required(login_url='/login'))
	def get(self,request):
		return render(request,'welcome.tpl')


class PostView(DetailView):
	@method_decorator(login_required(login_url='/login'))
	def get(self,request):
		context_dict = {}
		form = PostForm()

		context_dict['form'] = form

		return render(request,'newpost_template.tpl',context_dict)

	@method_decorator(login_required(login_url='/login'))
	def post(self,request):
		context_dict = {}

		form = PostForm(request.POST)
		import ipdb; ipdb.set_trace()

		if form.is_valid():
			post = form.save(commit=False)
			post.author_id = request.user.id
			post.publication_date = datetime.datetime.now()

		context_dict['form'] = form

		return render(request,'newpost_template.tpl',context_dict)
