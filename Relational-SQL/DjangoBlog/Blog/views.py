from django.shortcuts import render,render_to_response
from django.views.generic import ListView,DetailView
from .models import *
# Create your views here.


class Index(DetailView):

	def get(self,request):
		return render_to_response('welcome.tpl')
