from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
import secrets
import random


# Create your views here.

def home(request):
	if request.user.is_authenticated:
		return redirect('/dashboard')
	rand1 = str(random.randint(10000,99999))
	rand2 = str(random.randint(10000,99999))
	userNameGen = rand1 + rand2
	#userNameGen = secrets.token_hex(16)
	context = {'usr':userNameGen}
	return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')

def privacy(request):
    return render(request, 'home/privacy.html')
