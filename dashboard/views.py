from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.decorators import login_required

#db models
from django.contrib.auth.models import User
from site_settings.models import siteSettings, CurrentPrice
from wallet.models import proofs
from users.models import Users, Referrals, Cards
from transactions.models import transactions
from django.contrib.auth.models import AbstractUser
from wallet.models import wallets, AccountNums
from vendor.models import Vendors


#forms
from uploads.forms import uploadPOPForm

from django.contrib import messages

from datetime import datetime

import secrets
import random
#to do not equal to
from django.db.models import Q


siteSet = siteSettings.objects.filter(id='1').first()
current_price = CurrentPrice.objects.last()

@login_required(login_url='/login')
def dashboard(request):
	userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
	defaultAccount = AccountNums.objects.filter(user_id=request.user.id, type='NTC', label = 'Default').first()
	allAccount = AccountNums.objects.filter(user_id=request.user.id, type='NTC')

	getUser = Users.objects.filter(user_id = request.user.id).first()

	if getUser and getUser.firstname == None:
		return redirect('/settings/user')

	userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
	walletUSD = float(current_price.usd) * float(userWallet.balance)
	if AccountNums.objects.filter(number=request.user).exists() == False:
		AccountNums(label = 'Default', number = request.user, user_id=request.user.id, type=siteSet.symbol, balance = 0, sent = 0, received = 0, status = 1, date_added = datetime.now()).save()
	context = {'siteSet':siteSet, 'userWallet':userWallet, 'getUser':getUser, 'current_price':current_price,
	'userWallet':userWallet,
	'defaultAccount':defaultAccount,
	'allAccount':allAccount,
	'walletUSD':walletUSD}
	#upload proof of payment
	try:
		if request.method == 'POST' and request.FILES['pop']:
			rand1 = str(random.randint(10000,99999))
			rand2 = str(random.randint(10000,99999))
			TransId = rand1 + rand2
			form = uploadPOPForm(request.POST, request.FILES)
			if form.is_valid():
				pending_pop_ck = proofs.objects.filter(user_id=request.user.id, status=0).exists()
				if pending_pop_ck == False:
					uploadpath1 = "proofs/"
					uploadpath2 = str(request.FILES['pop'])
					uploadpath = uploadpath1 + uploadpath2
					#uploadCover = Profile.objects.filter(email=request.user.email, username=request.user).update(cover_pic = uploadpath)
					instance1 = proofs(user_id = request.user.id, pop = request.FILES['pop'], status = 0, date_added = datetime.now())
					instance2 = transactions(user_id = request.user.id, transaction_id = TransId, email = request.user.email, type = 'Deposit', status = 0, date_added = datetime.now())
					instance1.save()
					instance2.save()
					getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">Proof of payment sent. It will be reviewed soon and we will get back to you.</p></div>'
					messages.error(request, getMsg)
				if pending_pop_ck == True:
					getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">Sorry, you can not upload proof of payment at this time. We are still reviewing your last proof of payment.</p></div>'
					messages.error(request, getMsg)
					'''
					getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">Sorry, you can not upload proof of payment at this time. We are still reviewing your last proof of payment.</p></div>'
					response = {'msg':getMsg}
					return JsonResponse(response)
					'''
			else:
				getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">Upload failed. Please, try again.</p></div>'
				messages.error(request, getMsg)
	except:
		pass
	return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='/login')
def settings(request):
	checkRecs = Vendors.objects.filter(user_id = request.user.id).exists()
	if checkRecs == True:
		return redirect('/settings/vendor')
	else:
		return redirect('/settings/user')

	return render(request, 'dashboard/settings.html', context)

@login_required(login_url='/login')
def referral(request):
	userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
	defaultAccount = AccountNums.objects.filter(user_id=request.user.id, type='NTC', label = 'Default').first()
	allAccount = AccountNums.objects.filter(user_id=request.user.id, type='NTC')

	ref = Referrals.objects.filter(invitee=request.user.id)

	getUsers = User.objects.filter()
	getUser = Users.objects.filter(user_id = request.user.id).first()
	userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
	walletUSD = float(current_price.usd) * float(userWallet.balance)
	if AccountNums.objects.filter(number=request.user).exists() == False:
		AccountNums(label = 'Default', number = request.user, user_id=request.user.id, type=siteSet.symbol, balance = 0, sent = 0, received = 0, status = 1, date_added = datetime.now()).save()
	context = {'siteSet':siteSet, 'userWallet':userWallet, 'getUser':getUser, 'getUsers':getUsers, 'current_price':current_price,
	'userWallet':userWallet,
	'defaultAccount':defaultAccount,
	'allAccount':allAccount,
	'walletUSD':walletUSD,
	'ref':ref}
	return render(request, 'dashboard/referral.html', context)

@login_required(login_url='/login')
def credit_card(request):
	userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
	defaultAccount = AccountNums.objects.filter(user_id=request.user.id, type='NTC', label = 'Default').first()
	allAccount = AccountNums.objects.filter(user_id=request.user.id, type='NTC')

	ref = Referrals.objects.filter(invitee=request.user.id)

	getUser = Users.objects.filter(user_id = request.user.id).first()
	userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
	walletUSD = float(current_price.usd) * float(userWallet.balance)
	if AccountNums.objects.filter(number=request.user).exists() == False:
		AccountNums(label = 'Default', number = request.user, user_id=request.user.id, type=siteSet.symbol, balance = 0, sent = 0, received = 0, status = 1, date_added = datetime.now()).save()
	context = {'siteSet':siteSet, 'userWallet':userWallet, 'getUser':getUser, 'current_price':current_price,
	'userWallet':userWallet,
	'defaultAccount':defaultAccount,
	'allAccount':allAccount,
	'walletUSD':walletUSD,
	'ref':ref}
	return render(request, 'dashboard/credit_card.html', context)
