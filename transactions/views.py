from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

#password hash
from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.decorators import login_required

#db models
from django.contrib.auth.models import User
from vendor.models import Vendors
from users.models import Users
from wallet.models import proofs, AccountNums, wallets
from transactions.models import transactions
from django.contrib.auth.models import AbstractUser

from django.contrib import messages

from datetime import datetime

import secrets
import random

#to do not equal to
from django.db.models import Q

#data models
from site_settings.models import siteSettings, CurrentPrice

siteSet = siteSettings.objects.filter(id='1').first()
current_price = CurrentPrice.objects.last()

@login_required(login_url='/login')
def all_transactions(request):
	userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
	userTrans = transactions.objects.filter(user_id=request.user.id)
	context = {'siteSet':siteSet,
	'current_price':current_price,
	'userWallet':userWallet,
	'userTrans':userTrans}

	return render(request, 'transactions/transactions.html', context)

def view_transactions(request, id, transId):
    userTrans = transactions.objects.filter(id = id, transaction_id = transId).get()
    amtInUsd = float(current_price.usd) * float(userTrans.amount)

    context = {'siteSet':siteSet,
	'current_price':current_price,
	'userTrans':userTrans,
    'amtInUsd':amtInUsd}

    return render(request, 'transactions/view.html', context)
