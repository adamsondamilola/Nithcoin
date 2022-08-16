from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
#password hash
from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

#db models
from django.contrib.auth.models import User
from vendor.models import Vendors, PaymentMethods
from wallet.models import wallets
from users.models import Users

#forms
from uploads.forms import uploadProfile
from uploads.forms import uploadId

from django.contrib.auth.models import AbstractUser

from django.contrib import messages

from datetime import datetime

import secrets

#to do not equal to
from django.db.models import Q

#data models
from site_settings.models import siteSettings, CurrentPrice

#encrypt PIN
import bcrypt

siteSet = siteSettings.objects.filter(id='1').first()
current_price = CurrentPrice.objects.last()



@login_required(login_url='/login')
def accounts(request):
	userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
	context = {'siteSet':siteSet, 'userWallet':userWallet}
	return render(request, 'vendor/account_numbers.html', context)

@login_required(login_url='/login')
def vendor_info(request, id):
	userWallet = wallets.objects.filter(user_id = request.user.id, type='NTC').first()
	listVendors = Vendors.objects.filter(user_id = id, status=1).first()
	getUser = Users.objects.filter(user_id = request.user.id).first()
	curprice = int(current_price.usd)
	sell_usd = (int(listVendors.selling_at)/100 * curprice) + curprice
	buy_usd = (int(listVendors.buying_at)/100 * curprice) + curprice
	discount_sell = int((int(listVendors.selling_at)/20) * 100)
	discount_sell = 100 - discount_sell
	context = {'siteSet':siteSet,
	'userWallet':userWallet,
	'listVendors':listVendors,
	'sell_usd':sell_usd,
	'buy_usd':buy_usd,
	'discount_sell':discount_sell,
	'current_price':current_price,
	'getUser':getUser}
	return render(request, 'vendor/vendor.html', context)

@login_required(login_url='/login')
def vendor_info_(request, id):
	userWallet = wallets.objects.filter(user_id = request.user.id, type='NTC').first()
	listVendors = Vendors.objects.filter(user_id = id, status=1).first()
	getUser = Users.objects.filter(user_id = request.user.id).first()
	curprice = int(current_price.usd)
	sell_usd = (int(listVendors.selling_at)/100 * curprice) + curprice
	buy_usd = (int(listVendors.buying_at)/100 * curprice) + curprice
	discount_sell = int((int(listVendors.selling_at)/20) * 100)
	discount_sell = 100 - discount_sell
	context = {'siteSet':siteSet,
	'userWallet':userWallet,
	'listVendors':listVendors,
	'sell_usd':sell_usd,
	'buy_usd':buy_usd,
	'discount_sell':discount_sell,
	'current_price':current_price,
	'getUser':getUser}
	return render(request, 'vendor/vendor_sell.html', context)

@csrf_exempt
@login_required(login_url='/login')
def vendor_settings(request):
	payBank = PaymentMethods.objects.filter(user_id=request.user.id, method = 'Bank').first()
	payBitcoin = PaymentMethods.objects.filter(user_id=request.user.id, method = 'Bitcoin').first()
	payEtherium = PaymentMethods.objects.filter(user_id=request.user.id, method = 'Etherium').first()
	payPayPal = PaymentMethods.objects.filter(user_id=request.user.id, method = 'PayPal').first()
	payPayza = PaymentMethods.objects.filter(user_id=request.user.id, method = 'Payza').first()
	payMobile = PaymentMethods.objects.filter(user_id=request.user.id, method = 'Mobile Money').first()
	payChipper = PaymentMethods.objects.filter(user_id=request.user.id, method = 'Chipper Cash').first()

	status = 1
	checkRecs = Vendors.objects.filter(user_id = request.user.id).exists()
	if checkRecs == False:
		return redirect('/dashboard')
	getVendor = Vendors.objects.filter(user_id = request.user.id).first()
	userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
	context = {'siteSet':siteSet, 'userWallet':userWallet, 'getVendor': getVendor, 'payBank':payBank, 'payBitcoin':payBitcoin, 'payEtherium':payEtherium, 'payPayPal':payPayPal, 'payPayza':payPayza, 'payMobile':payMobile, 'payChipper':payChipper, 'current_price':current_price}

	try:
		if request.method == 'POST' and request.FILES['profile']:
			form = uploadProfile(request.POST, request.FILES)
			if form.is_valid():
				uploadpath1 = "vendors/"
				uploadpath2 = str(request.FILES['profile'])
				uploadpath = uploadpath1 + uploadpath2
				updateRec = Vendors.objects.filter(user_id=request.user.id).update(profile = uploadpath)
				form.save()
				return redirect('/settings/vendor')
			else:
				msgOutput = 'An error occurred uploading. Please, try again'
				getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				messages.error(request, getMsg)
	except:
		pass
		'''
		msgOutput = 'An error occurred. Please, try again'
		getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
		messages.error(request, getMsg)
		'''

	#logout devices
	if request.method == 'POST' and request.POST.get('logout_devices'):
		from auth_user.models import userlogs
		userDevice = request.META['HTTP_USER_AGENT']
		checkLogs = userlogs.objects.filter(user_id=request.user.id).exclude(device=userDevice).exists()
		if checkLogs == True:
			userlogs.objects.filter(user_id=request.user.id).exclude(device=userDevice).delete()
			msgOutput = 'Devices Logged Out!'
			getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			response = {'msg':getMsg}
			return JsonResponse(response)
		else:
			msgOutput = 'You are already logged out of other devices'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			response = {'status':0, 'msg':getMsg}
			return JsonResponse(response)

	#reset password
	if request.method == 'POST' and request.POST.get('reset_password'):
		checkPassword = check_password(request.POST.get('password'), request.user.password)
		newPassword = make_password(request.POST.get('password1'))
		if checkPassword == False:
			msgOutput = 'Password is invalid'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			#response = {'status':0, 'msg':getMsg}
			#return JsonResponse(response)
			messages.error(request, getMsg)
		elif len(request.POST.get('password1')) < 6 or len(request.POST.get('password2')) < 6:
			msgOutput = 'Password should be at least 6 characters'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			#response = {'status':0, 'msg':getMsg}
			#return JsonResponse(response)
			messages.error(request, getMsg)
		elif request.POST.get('password') == "" or request.POST.get('password1') == "" or request.POST.get('password2') == "":
			msgOutput = 'Password can not be empty'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			#response = {'status':0, 'msg':getMsg}
			#return JsonResponse(response)
			messages.error(request, getMsg)
		elif request.POST.get('password1') != request.POST.get('password2'):
			msgOutput = 'New Password do not match'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			#response = {'status':0, 'msg':getMsg}
			#return JsonResponse(response)
			messages.error(request, getMsg)
		else:
			updatePassword = User.objects.filter(username=request.user).update(password = newPassword)
			if updatePassword:
				msgOutput = 'Password was successfully changed'
				getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				messages.error(request, getMsg)


	#new PIN
	if request.method == 'POST' and request.POST.get('new_pin'):
		if len(request.POST.get('pin1')) < 4 or len(request.POST.get('pin2')) < 4:
			msgOutput = 'PIN should be 4 digits'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			messages.error(request, getMsg)
		elif len(request.POST.get('pin1')) > 4 or len(request.POST.get('pin2')) > 4:
			msgOutput = 'PIN should not be more than 4 digits'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			messages.error(request, getMsg)
		elif request.POST.get('pin1') != request.POST.get('pin2'):
			msgOutput = 'PIN do not match'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			messages.error(request, getMsg)
		elif type(int(request.POST.get('pin1'))) != int or type(int(request.POST.get('pin2'))) != int:
			msgOutput = 'PIN should be numbers'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			messages.error(request, getMsg)
		else:
			newPin = make_password(request.POST.get('pin1'))
			updatePin = wallets.objects.filter(user_id=request.user.id).update(pin = newPin)
			if updatePin:
				msgOutput = 'PIN Created!'
				getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				messages.info(request, getMsg)

	#update PIN
	if request.method == 'POST' and request.POST.get('reset_pin'):
		checkPin = check_password(request.POST.get('pin'), userWallet.pin)
		if checkPin == False:
			msgOutput = 'PIN is invalid'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			messages.error(request, getMsg)
		elif len(request.POST.get('pin1')) < 4 or len(request.POST.get('pin2')) < 4:
			msgOutput = 'PIN should be 4 digits'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			messages.error(request, getMsg)
		elif len(request.POST.get('pin1')) < 4 or len(request.POST.get('pin2')) < 4:
			msgOutput = 'PIN should be 4 digits'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			messages.error(request, getMsg)
		elif len(request.POST.get('pin1')) > 4 or len(request.POST.get('pin2')) > 4:
			msgOutput = 'PIN should not be more than 4 digits'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			messages.error(request, getMsg)
		elif request.POST.get('pin1') != request.POST.get('pin2'):
			msgOutput = 'PIN do not match'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			messages.error(request, getMsg)
		elif type(int(request.POST.get('pin1'))) != int or type(int(request.POST.get('pin2'))) != int:
			msgOutput = 'PIN should be numbers'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			messages.error(request, getMsg)
		else:
			newPin = make_password(request.POST.get('pin'))
			updatePin = wallets.objects.filter(user_id=request.user.id).update(pin = newPin)
			if updatePin:
				msgOutput = 'PIN Successfully Updated!'
				getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				messages.info(request, getMsg)

	#update buy and sell
	if request.method == 'POST' and request.POST.get('buy_sell'):
		if request.POST.get('minimum') == '':
			msgOutput = 'Please, enter minimum amount'
			getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			response = {'msg':getMsg}
			return JsonResponse(response)
		else:
			Vendors.objects.filter(user_id=request.user.id).update(minimum = request.POST.get('minimum'), selling_at = request.POST.get('selling_at'), buying_at = request.POST.get('buying_at'))
			msgOutput = 'Settings Updated!'
			getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
			response = {'msg':getMsg}
			return JsonResponse(response)

	#update payment method
	if request.method == 'POST' and request.POST.get('paymentmode'):
		if request.method == 'POST' and request.POST.get('bitcoin'):
			typeSelected1 = 'Bitcoin'
			checkMethods = PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected1).exists()
			if checkMethods == False:
				instance = PaymentMethods(user_id=request.user.id, method = typeSelected1, date_added = datetime.now())
				instance.save()
			else:
				PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected1).delete()

		if request.method == 'POST' and request.POST.get('etherium'):
			typeSelected2 = 'Etherium'
			checkMethods = PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected2).exists()
			if checkMethods == False:
				instance = PaymentMethods(user_id=request.user.id, method = typeSelected2, date_added = datetime.now())
				instance.save()
			else:
				PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected2).delete()

		if request.method == 'POST' and request.POST.get('bank'):
			typeSelected3 = 'Bank'
			checkMethods = PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected3).exists()
			if checkMethods == False:
				instance = PaymentMethods(user_id=request.user.id, method = typeSelected3, date_added = datetime.now())
				instance.save()
			else:
				PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected3).delete()

		if request.method == 'POST' and request.POST.get('mobile_money'):
			typeSelected4 = 'Mobile Money'
			checkMethods = PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected4).exists()
			if checkMethods == False:
				instance = PaymentMethods(user_id=request.user.id, method = typeSelected4, date_added = datetime.now())
				instance.save()
			else:
				PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected4).delete()

		if request.method == 'POST' and request.POST.get('chipper_cash'):
			typeSelected5 = 'Chipper Cash'
			checkMethods = PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected5).exists()
			if checkMethods == False:
				instance = PaymentMethods(user_id=request.user.id, method = typeSelected5, date_added = datetime.now())
				instance.save()
			else:
				PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected5).delete()

		if request.method == 'POST' and request.POST.get('paypal'):
			typeSelected6 = 'PayPal'
			checkMethods = PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected6).exists()
			if checkMethods == False:
				instance = PaymentMethods(user_id=request.user.id, method = typeSelected6, date_added = datetime.now())
				instance.save()
			else:
				PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected6).delete()

		if request.method == 'POST' and request.POST.get('payza'):
			typeSelected7 = 'Payza'
			checkMethods = PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected7).exists()
			if checkMethods == False:
				instance = PaymentMethods(user_id=request.user.id, method = typeSelected7, date_added = datetime.now())
				instance.save()
			else:
				PaymentMethods.objects.filter(user_id = request.user.id, method=typeSelected7).delete()


	return render(request, 'vendor/settings.html', context)

@login_required(login_url='/login')
def newvendor(request):
	status = 1
	userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
	getVendor = Vendors.objects.filter(user_id = request.user.id).first()
	checkRecs = Vendors.objects.filter(user_id = request.user.id).exists()
	context = {'siteSet':siteSet, 'getVendor':getVendor, 'checkRecs':checkRecs, 'userWallet':userWallet}
	if checkRecs == False:
		#return redirect('/')
		if request.method == 'POST' and request.POST.get('step1'):
			vendor = Vendors()
			firstname = request.POST.get('firstname')
			lastname = request.POST.get('lastname')
			country = request.POST.get('country')
			city = request.POST.get('city')
			#check input errs
			if len(firstname) < 2 or len(firstname) < 2:
				status = 0
				msgOutput = 'Name too short or empty'
				getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				response = {'status':0, 'msg':getMsg}
				return JsonResponse(response)
			if firstname.isalpha() == False:
				status = 0
				msgOutput = 'Name should be alphabets and without space'
				getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				response = {'status':0, 'msg':getMsg}
				return JsonResponse(response)
			if lastname.isalpha() == False:
				status = 0
				msgOutput = 'Name should be alphabets and without space'
				getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				response = {'status':0, 'msg':getMsg}
				return JsonResponse(response)
			if len(city)< 2:
				status = 0
				msgOutput = 'City name too short or empty'
				getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				response = {'status':0, 'msg':getMsg}
				return JsonResponse(response)
			if country == '':
				status = 0
				msgOutput = 'Please select a country'
				getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				response = {'status':0, 'msg':getMsg}
				return JsonResponse(response)
			if status == 1:
				vendor.firstname = firstname
				vendor.lastname = lastname
				vendor.country = country
				vendor.city = city
				vendor.status = 0
				vendor.email = request.user.email
				vendor.user_id = request.user.id
				vendor.date_added = datetime.now()
				vendor.save()
				msgOutput = 'Saved!'
				getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				response = {'status':1, 'msg':getMsg}
				return JsonResponse(response)

	if checkRecs == True:
		if request.method == 'POST' and request.POST.get('step2'):
			#form = uploadProfile(request.POST, request.FILES)
			mobile = request.POST.get('mobile')
			whatsapp = request.POST.get('whatsapp')
			if len(mobile) < 8:
				status = 0
				msgOutput = 'Please, enter a valid mobile contact'
				getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				response = {'status':0, 'msg':getMsg}
				return JsonResponse(response)
			if len(whatsapp) < 8:
				status = 0
				msgOutput = 'Please, enter a valid WhatsApp contact'
				getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				response = {'status':0, 'msg':getMsg}
				return JsonResponse(response)
			if mobile[0] != '+' or whatsapp[0] != '+':
				status = 0
				msgOutput = 'Number should be in international format. Starting with + '
				getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				response = {'status':0, 'msg':getMsg}
				return JsonResponse(response)
			#if form.is_valid() and status == 1:
			if status == 1:
				#updateRec = Vendors.objects.filter(user_id=request.user.id).update(mobile = mobile, whatsapp = whatsapp, profile = request.FILES['profile'])
				updateRec = Vendors.objects.filter(user_id=request.user.id).update(mobile = mobile, whatsapp = whatsapp)
				msgOutput = 'Saved!'
				getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				response = {'status':1, 'msg':getMsg}
				return JsonResponse(response)

	try:
		if request.method == 'POST' and request.POST.get('step3'):
			form = uploadId(request.POST, request.FILES)
			if form.is_valid():
				#form.save()
				updateRec = Vendors.objects.filter(user_id=request.user.id).update(id_card = request.FILES['id_card'])
				return redirect('/newvendor')
			else:
				msgOutput = 'An error occurred. Please, try again'
				getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
				messages.error(request, getMsg)
	except:
		pass
		'''
		msgOutput = 'An error occurred. Please, try again'
		getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
		messages.error(request, getMsg)
		'''

	return render(request, 'vendor/newvendor.html', context)
