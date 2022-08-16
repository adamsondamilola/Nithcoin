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
from .models import Users
from vendor.models import Vendors
from wallet.models import wallets

#forms
from uploads.forms import uploadProfile_User
from uploads.forms import uploadId_User

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
def user_settings(request):
    getUser = Users.objects.filter(user_id = request.user.id).first()
    userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
    context = {'siteSet':siteSet, 'userWallet':userWallet, 'getUser':getUser}
    checkRecs = Vendors.objects.filter(user_id = request.user.id).exists()
    status = 1

    if checkRecs == True:
        return redirect('/settings/vendor')
    else:
        if Users.objects.filter(user_id = request.user.id).exists() == False:
            Users(user_id=request.user.id, email = request.user.email, date_added = datetime.now()).save()

        try:
            if request.method == 'POST' and request.FILES['profile']:
                form = uploadProfile_User(request.POST, request.FILES)
                if form.is_valid():
                    uploadpath1 = "users/"
                    uploadpath2 = str(request.FILES['profile'])
                    uploadpath = uploadpath1 + uploadpath2
                    updateRec = Users.objects.filter(user_id=request.user.id).update(profile = uploadpath)
                    form.save()
                    return redirect('/settings/user')
                else:
                    msgOutput = 'An error occurred uploading. Please, try again'
                    getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
                    messages.error(request, getMsg)
        except:
            pass

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
                    getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
                    messages.error(request, getMsg)
                    return redirect('/settings/user')


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

    if request.method == 'POST' and request.POST.get('update_profile'):
        mobile = request.POST.get('mobile')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        country = request.POST.get('country')
        city = request.POST.get('city')
        if len(mobile) < 8:
            status = 0
            msgOutput = 'Please, enter a valid mobile contact'
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
            response = {'status':0, 'msg':getMsg}
            return JsonResponse(response)
        if mobile[0] != '+':
            status = 0
            msgOutput = 'Number should be in international format. Starting with + '
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
            response = {'status':0, 'msg':getMsg}
            return JsonResponse(response)
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
            updateRec = Users.objects.filter(user_id=request.user.id).update(mobile = mobile,
            firstname = firstname, lastname = lastname, country = country, city = city)
            msgOutput = 'Saved!'
            getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
            response = {'status':1, 'msg':getMsg}
            return JsonResponse(response)

    return render(request, 'users/settings.html', context)
