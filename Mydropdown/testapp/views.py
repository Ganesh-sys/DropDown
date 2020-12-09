from django.shortcuts import render,redirect
from .models import *
#from django.contrib.auth import authenticate,login,logout
#from django.contrib.auth.models import User

# Create your views here.
	
def index(request):
	program=Programming.objects.all()
	context={'program':program}
	return render(request,'index.html',context)

def load_courses(request):
	programming_id=request.GET.get('programming')
	courses=Course.objects.filter(programming_id=programming_id).order_by('name')
	return render(request,'courses_dropdown_list_options.html',{'courses':courses})