from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.decorators import login_required

#db models
from django.contrib.auth.models import User, AbstractUser
from site_settings.models import siteSettings
from wallet.models import proofs, AccountNums, wallets
from transactions.models import transactions
from vendor.models import Vendors

#forms
from uploads.forms import uploadPOPForm

from django.contrib import messages

from datetime import datetime

import secrets
import random
#to do not equal to
from django.db.models import Q

#QRCode
'''
import qrcode
qr = qrcode.make('hello')
qr.save('qrcode.png')

qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
)

data = 'your text here'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('<file name>.png')
'''

siteSet = siteSettings.objects.filter(id='1').first()
# siteSet.symbol is currency default

@login_required(login_url='/login')
def numbers(request):
    userWallet = wallets.objects.filter(user_id=request.user.id, type=siteSet.symbol).first()

    userAccounts = AccountNums.objects.filter(user_id=request.user.id, type=siteSet.symbol)

    userInfo = User.objects.filter(username=request.user).first()

    context = {'siteSet':siteSet, 'userWallet':userWallet, 'userAccounts':userAccounts, 'userInfo':userInfo}

    if request.method == 'POST' and request.POST.get('new_account'):
        label_ = request.POST.get('label')

        if len(label_) > 25:
            msgOutput = 'Label should not be more than 25 characters.'
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
            messages.error(request, getMsg)

        if label_ == '':
            msgOutput = 'Label should not be empty.'
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
            messages.error(request, getMsg)

        else:
            rand1 = str(random.randint(10000,99999))
            rand2 = str(random.randint(10000,99999))
            newGenerated = rand1 + rand2
            acct_exists = User.objects.filter(username=newGenerated).exists()
            if acct_exists == False:
                instance = AccountNums(label = label_, number = newGenerated, user_id=request.user.id, type=siteSet.symbol, balance = 0, sent = 0, received = 0, status = 1, date_added = datetime.now()).save()
                msgOutput = 'New Account Number Created! <b>'+newGenerated+'</b>'
                getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
                messages.error(request, getMsg)
            else:
                msgOutput = 'An error occurred, please try again.'
                getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
                messages.error(request, getMsg)

    return render(request, 'account/numbers.html', context)

@login_required(login_url='/login')
def view_number(request, num):
    userWallet = wallets.objects.filter(user_id=request.user.id, type=siteSet.symbol).first()
    userAccounts = AccountNums.objects.filter(number=num).first()
    userInfo = User.objects.filter(username=request.user).first()
    context = {'siteSet':siteSet, 'userWallet':userWallet, 'userAccounts':userAccounts, 'userInfo':userInfo}
    return render(request, 'account/view_number.html', context)
