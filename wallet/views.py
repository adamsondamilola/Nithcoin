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
def wallet(request):
	getUser = Users.objects.filter(user_id = request.user.id).first()
	context = {'siteSet':siteSet, 'getUser':getUser}
	return render(request, 'wallet/wallet.html', context)


@login_required(login_url='/login')
def buy(request):
	getUser = Users.objects.filter(user_id = request.user.id).first()
	context = {'siteSet':siteSet, 'getUser':getUser}
	if request.method == 'POST' and request.POST.get('country'):
		vendorCountry = request.POST.get('country')
		checkRecs = Vendors.objects.filter(status=1, country = vendorCountry).exists()
		if checkRecs == False:
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages"><b>No result found!</b></p><p>You may check back again or apply to become a vendor in </p>'+vendorCountry+' by clicking the button below </div><br><a href="/newvendor"><button type="submit" class="btn btn-primary btn-lg btn-block">Become a Vendor</button></a>'
			response = {'status':0, 'msg':getMsg}
			return JsonResponse(response)
		if checkRecs == True:
			#listVendors = Vendors.objects.filter(status=1, country = vendorCountry)[:5]
			getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">Result Found!</p></div>'
			messages.info(request, getMsg)
			response = {'status':1, 'msg':getMsg}
			return JsonResponse(response)
	return render(request, 'wallet/buy.html', context)


@login_required(login_url='/login')
def search_seller(request, countryname):
	getUser = Users.objects.filter(user_id = request.user.id).first()
	context = {'siteSet':siteSet, 'getUser':getUser}
	curprice = int(current_price.usd)
	listVendors = Vendors.objects.filter(status=1, country = countryname) #.all()[:4]
	checkRecs = Vendors.objects.filter(status=1, country = countryname).exists()
	context = {'siteSet':siteSet,
	'listVendors':listVendors,
	'getUser':getUser,
	'current_price':current_price}
	if checkRecs == False:
		return redirect('/buy')
		getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages"><b>No result found!</b></p></div>'
		messages.error(request, getMsg)
	return render(request, 'wallet/buy.html', context)

@login_required(login_url='/login')
def search_buyer(request, countryname):
	getUser = Users.objects.filter(user_id = request.user.id).first()
	context = {'siteSet':siteSet, 'getUser':getUser}
	curprice = int(current_price.usd)
	listVendors = Vendors.objects.filter(status=1, country = countryname) #.all()[:4]
	checkRecs = Vendors.objects.filter(status=1, country = countryname).exists()
	context = {'siteSet':siteSet,
	'listVendors':listVendors,
	'getUser':getUser,
	'current_price':current_price}
	if checkRecs == False:
		return redirect('/sell')
		getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages"><b>No result found!</b></p></div>'
		messages.error(request, getMsg)
	return render(request, 'wallet/sell.html', context)

@login_required(login_url='/login')
def sell(request):
	getUser = Users.objects.filter(user_id = request.user.id).first()
	context = {'siteSet':siteSet, 'getUser':getUser}
	if request.method == 'POST' and request.POST.get('country'):
		vendorCountry = request.POST.get('country')
		checkRecs = Vendors.objects.filter(status=1, country = vendorCountry).exists()
		if checkRecs == False:
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages"><b>No result found!</b></p><p>You may check back again or apply to become a vendor in </p>'+vendorCountry+' by clicking the button below </div><br><a href="/newvendor"><button type="submit" class="btn btn-primary btn-lg btn-block">Become a Vendor</button></a>'
			response = {'status':0, 'msg':getMsg}
			return JsonResponse(response)
		if checkRecs == True:
			#listVendors = Vendors.objects.filter(status=1, country = vendorCountry)[:5]
			getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">Result Found!</p></div>'
			messages.info(request, getMsg)
			response = {'status':1, 'msg':getMsg}
			return JsonResponse(response)
	return render(request, 'wallet/sell.html', context)

@login_required(login_url='/login')
def send(request):
	userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
	defaultAccount = AccountNums.objects.filter(user_id=request.user.id, type='NTC', label = 'Default').first()
	allAccount = AccountNums.objects.filter(user_id=request.user.id, type='NTC')
	context = {'siteSet':siteSet,
	'current_price':current_price,
	'userWallet':userWallet,
	'defaultAccount':defaultAccount,
	'allAccount':allAccount}
	if request.method == 'POST' and request.POST.get('send'):
		getAmount = float(request.POST.get('amount'))
		getAmountNTC = getAmount/int(current_price.usd)
		getNum = request.POST.get('account_number')

		wallet_addr = request.POST.get('wallet')
		x = AccountNums.objects.filter(user_id=request.user.id, type='NTC', number = wallet_addr).first()
		walletAcct = float(x.balance)

		if walletAcct < getAmountNTC:
			errMsg = 'Insufficient fund'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button> '+errMsg+' </div>'
			response = {'status':0, 'msg':getMsg}
			return JsonResponse(response)
		elif AccountNums.objects.filter(number=getNum).exists() == False:
			errMsg = 'Account number not fund'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button> '+errMsg+' </div>'
			response = {'status':0, 'msg':getMsg}
			return JsonResponse(response)
		elif AccountNums.objects.filter(number=getNum, user_id = request.user.id).exists() == True:
			errMsg = 'You can not transfer fund to self.'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button> '+errMsg+' </div>'
			response = {'status':0, 'msg':getMsg}
			return JsonResponse(response)
		else:
			errMsg = 'Please, wait...'
			getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button> '+errMsg+' </div>'
			response = {'status':1, 'msg':getMsg}
			return JsonResponse(response)
	return render(request, 'wallet/send.html', context)

@login_required(login_url='/login')
def confirm_send(request, amt, acc, wal):
	userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
	defaultAccount = AccountNums.objects.filter(user_id=request.user.id, type='NTC', label = 'Default').first()
	allAccount = AccountNums.objects.filter(user_id=request.user.id, type='NTC')
	context = {'siteSet':siteSet,
	'current_price':current_price,
	'userWallet':userWallet,
	'defaultAccount':defaultAccount,
	'allAccount':allAccount,
	'amt':amt,
	'acc':acc}
	if request.method == 'POST' and request.POST.get('confirm_send'):
		getAmount = float(amt)
		getAmountNTC = getAmount/int(current_price.usd)
		getNum = acc

		wallet_addr = wal
		x = AccountNums.objects.filter(user_id=request.user.id, type='NTC', number = wallet_addr).first()
		walletAcct = float(x.balance)

		if walletAcct < getAmountNTC:
			errMsg = 'Insufficient fund'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button> '+errMsg+' </div>'
			response = {'status':0, 'msg':getMsg}
			return JsonResponse(response)
		elif AccountNums.objects.filter(number=getNum).exists() == False:
			errMsg = 'Account number not fund'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button> '+errMsg+' </div>'
			response = {'status':0, 'msg':getMsg}
			return JsonResponse(response)
		elif check_password(request.POST.get('pin'), userWallet.pin) == False:
			errMsg = 'Invalid transaction PIN'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button> '+errMsg+' </div>'
			response = {'status':0, 'msg':getMsg}
			return JsonResponse(response)
		elif AccountNums.objects.filter(number=getNum, user_id = request.user.id).exists() == True:
			errMsg = 'You can not transfer fund to self.'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button> '+errMsg+' </div>'
			response = {'status':0, 'msg':getMsg}
			return JsonResponse(response)
		else:
			rand1 = str(random.randint(10000,99999))
			rand2 = str(random.randint(10000,99999))
			rand3 = str(random.randint(10000,99999))
			TransId = rand1 + rand2 + rand3
			#withdraw from sender
			a = AccountNums.objects.filter(user_id=request.user.id, number=wallet_addr).get()
			acctBal_a = a.balance - getAmountNTC
			sentBal = a.sent + getAmountNTC
			up1 = AccountNums.objects.filter(user_id=request.user.id, number=wallet_addr).update(balance = acctBal_a, sent = sentBal)

			w = wallets.objects.filter(user_id = request.user.id).get()
			acctBal_w = w.balance - getAmountNTC
			sentBal_w = w.sent + getAmountNTC
			up2 = wallets.objects.filter(user_id = request.user.id).update(balance = acctBal_w, sent = sentBal_w)

			transactions(user_id = request.user.id, receiver = getNum, sender = wallet_addr, transaction_id = TransId, email = request.user.email, amount = getAmountNTC, type = 'Sent', status = 1, date_added = datetime.now()).save()

			if up1 and up2:
				#add to receiver wallet
				a = AccountNums.objects.filter(number=getNum).first()
				acctBal_a = a.balance + getAmountNTC
				receivedBal = a.sent + getAmountNTC
				up3 = AccountNums.objects.filter(number=getNum).update(balance = acctBal_a, received = receivedBal)

				w = wallets.objects.filter(user_id = a.user_id).get()
				acctBal_w = w.balance + getAmountNTC
				receivedBal_w = w.received + getAmountNTC
				up4 = wallets.objects.filter(user_id = a.user_id).update(balance = acctBal_w, received = receivedBal_w)

				transactions(user_id = a.user_id, transaction_id = TransId, receiver = getNum, sender = wallet_addr, type = 'Received', status = 1, amount = getAmountNTC, date_added = datetime.now()).save()
			if up3 and up4:
				errMsg = 'Transaction was Successful'
				getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button> '+errMsg+' </div>'
				response = {'status':2, 'msg':getMsg}
				return JsonResponse(response)
			else:
				errMsg = 'Transaction failed'
				getMsg = '<div class="alert alert-daner alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button> '+errMsg+' </div>'
				response = {'status':0, 'msg':getMsg}
				return JsonResponse(response)

	return render(request, 'wallet/send.html', context)

@login_required(login_url='/login')
def swap(request):
	context = {'siteSet':siteSet}
	return render(request, 'wallet/swap.html', context)

@login_required(login_url='/login')
def receive(request):
	context = {'siteSet':siteSet}
	return redirect('account/numbers')

@login_required(login_url='/login')
def withdraw(request):
	context = {'siteSet':siteSet}
	return render(request, 'wallet/withdraw.html', context)
