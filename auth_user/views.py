from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from datetime import datetime

# Create your views here.
from .forms import CreateUserForm
import secrets
import random

#import database
from django.contrib.auth.models import User
from site_settings.models import siteSettings
from wallet.models import proofs, AccountNums, wallets
from .models import userlogs, ResetPassword
from users.models import Referrals

#For sending Mails
from nithcoin.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
fromMail = 'no_reply@nithcoin.com'

siteSet = siteSettings.objects.filter(id='1').first()

import ipapi

#password hash
from django.contrib.auth.hashers import make_password, check_password

#commission per referral
commissn = 0.001

def signup(request):
    userIp = request.META['REMOTE_ADDR']
    userCountry = ipapi.location(ip=userIp, output='country_name')
    userDevice = request.META['HTTP_USER_AGENT']
    #userNameGen = secrets.token_hex(16)
    rand1 = str(random.randint(10000,99999))
    rand2 = str(random.randint(10000,99999))
    userNameGen = rand1 + rand2
    form = CreateUserForm(initial={'username': userNameGen})
    #data = {}
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        form = CreateUserForm(request.POST)
        ckEmail = User.objects.filter(email=email).exists()

        if ckEmail == True:
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">Email address already in use.</p></div>'
            response = {'msg':getMsg}
            return JsonResponse(response)

        elif password1 != password2:
#            getMsg = messages.info(request, 'Failed! Password do not match')
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">Password do not match</p></div>'
            response = {'msg':getMsg}
            return JsonResponse(response)
        if form.is_valid():
            form.save()
            newUser = User.objects.filter(email=email).first()

            '''
            subject, from_email, to = 'Welcome to Nithcoin', fromMail, email
            text_content = 'This is an important message.'
            html_content = '<h4>NITHCOIN</h4><hr>Indeed, you have taken the right step for better future. Below is your primary account number<br><br><b>' +newUser.username+ '</b><br><br>You can use your account number to login, send, and receive funds from anywhere in the world.<br> Best Regards'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            '''
            
            if newUser:
                userLog = userlogs(user_id=newUser.id, ip=userIp, country = userCountry, device = userDevice,  date_added = datetime.now())
                userLog.save()

            getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages"><b>Account created.</b> We have sent your account number to your email address. You can login in with your account number and password. </p></div>'
            response = {'msg':getMsg}
            return JsonResponse(response)
            '''
            username = User.objects.get(email=email)
            #auto login after sign up
            user = authenticate(request, username=username.username, password=password1)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            '''
        else:
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">Failed! Please try again<br><b>Tips:</b> Password should have at least 1 number, 1 special character and 1 Uppercase letter</p></div>'
            response = {'msg':getMsg}
            return JsonResponse(response)

    context = {"form":form, "siteSet":siteSet}
    return render(request, "auth_user/signup.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        userIp = request.META['REMOTE_ADDR']
        userCountry = ipapi.location(ip=userIp, output='country_name')
        userDevice = request.META['HTTP_USER_AGENT']
        if request.method == 'POST':
            account_number = request.POST.get('account_number')
            password = request.POST.get('password')
            user = authenticate(request, username=account_number, password=password)
            if user is not None:
                logUser = User.objects.filter(username=account_number).first()
                ref = Referrals.objects.filter(invited = logUser.id, is_verified = 0)
                if ref.exists() == True:
                    ref_ = ref.first()
                    bal = wallets.objects.filter(user_id = ref_.invitee).first()
                    newbal = bal.commission + commissn
                    wallets.objects.filter(user_id = ref_.invitee).update(commission = newbal)
                    ref.update(is_verified = 1)
                userLog_exists = userlogs.objects.filter(user_id=logUser.id, ip=userIp, country = userCountry, device = userDevice).exists()
                if userLog_exists == False:
                    userLog = userlogs(user_id=logUser.id, ip=userIp, country = userCountry, device = userDevice,  date_added = datetime.now())
                    userLog.save()
                wallet_exists = wallets.objects.filter(user_id=logUser.id).exists()
                if wallet_exists == False:
                    createWallet = wallets(user_id=logUser.id, type=siteSet.symbol, balance = 0, sent = 0, received = 0, commission = 0, status = 1, date_added = datetime.now())
                    createWallet.save()
                login(request, user)
                getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">Login was success. Please, wait...</p></div>'
                response = {'status':1, 'msg':getMsg}
                return JsonResponse(response)
                #login(request, user)
                #return redirect('/dashboard')
            else:
                getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">Wrong account number or password</p></div>'
                response = {'msg':getMsg}
                return JsonResponse(response)

    context = {"siteSet":siteSet}
    return render(request, 'auth_user/login.html', context)

def invite(request, invitee):
    from users.models import Users, Referrals
    from vendor.models import Vendors
    ckRef = User.objects.filter(username = invitee).exists()
    if ckRef == False:
        return HttpResponse('Invalid referral link')
    ref = User.objects.filter(username = invitee).first()

    checkProfile = Users.objects.filter(user_id = ref.id).exists()
    if checkProfile == False:
        inviteeProfile = Vendors.objects.filter(user_id = ref.id).first()
    else:
        inviteeProfile = Users.objects.filter(user_id = ref.id).first()

    userIp = request.META['REMOTE_ADDR']
    userCountry = ipapi.location(ip=userIp, output='country_name')
    userDevice = request.META['HTTP_USER_AGENT']
    #userNameGen = secrets.token_hex(16)
    rand1 = str(random.randint(10000,99999))
    rand2 = str(random.randint(10000,99999))
    userNameGen = rand1 + rand2
    form = CreateUserForm(initial={'username': userNameGen})
    #data = {}
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        form = CreateUserForm(request.POST)
        if password1 != password2:
#            getMsg = messages.info(request, 'Failed! Password do not match')
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">Failed! Password do not match</p></div>'
            messages.error(request, getMsg)
        if form.is_valid():
            form.save()
            newUser = User.objects.filter(email=email).first()

            if newUser:
                saveref = Referrals(invitee=ref.id, invited=newUser.id, status = 0, date_added = datetime.now())
                saveref.save()

                userLog = userlogs(user_id=newUser.id, ip=userIp, country = userCountry, device = userDevice,  date_added = datetime.now())
                userLog.save()

            getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages"><b>Account created.</b> However, we have sent your account number to your email address. You can login in with your account number and password. </p></div>'
            messages.info(request, getMsg)
        else:
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">Failed! Please try again<br><b>Tips:</b> Password should have at least 1 number, 1 special character and 1 Uppercase letter</p></div>'
            messages.error(request, getMsg)

    context = {"form":form, "siteSet":siteSet, 'inviteeProfile':inviteeProfile, 'invitee':invitee}
    return render(request, "auth_user/invite.html", context)

def reset(request):
    context = {"siteSet":siteSet}
    if request.method == 'POST' and request.POST.get('email'):
        email = request.POST.get('email')
        ckUser = User.objects.filter(email = email).exists()
        if email == '':
            Msg = 'Email address can not be empty'
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">'+Msg+'</p></div>'
            messages.error(request, getMsg)
        elif ckUser == False:
            Msg = 'Account not found!'
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages"> '+Msg+'</p></div>'
            messages.error(request, getMsg)
        else:
            Userinfo = User.objects.filter(email=email).first()
            saveTemp = ResetPassword(user_id = Userinfo.id, email=email, status = 0, temp_password = '', unique = secrets.token_hex(16), code = secrets.token_hex(16), date_added = datetime.now())
            saveTemp_ = saveTemp.save()
            getUniqueId = ResetPassword.objects.filter(email=email).latest('id')
            link = '/reset/'+getUniqueId.unique+''
            response = '<script> window.location.replace("'+link+'"); </script>'
            return HttpResponse(response)

    return render(request, 'auth_user/reset.html', context)

def reset_pass(request, unique):
    context = {"siteSet":siteSet}

    ckUser = ResetPassword.objects.filter(code = unique).first()
    ckUser_ = ResetPassword.objects.filter(code = unique).exists()
    if ckUser_ == False:
        return HttpResponse('Sorry, we can not continue with the process')

    if request.method == 'POST' and request.POST.get('password'):
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == '' or password2 == '':
            Msg = 'Password can not be empty'
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages"> '+Msg+'</p></div>'
            messages.error(request, getMsg)
        elif len(password) < 6 or len(password2) < 6:
            Msg = 'Password should be at least 6 characters'
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages"> '+Msg+'</p></div>'
            messages.error(request, getMsg)
        elif password != password2:
            Msg = 'Passwords do not match'
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages"> '+Msg+'</p></div>'
            messages.error(request, getMsg)
        else:
            #Userinfo = User.objects.filter(email=email).first()
            updateRec = ResetPassword.objects.filter(unique=unique).update(temp_password = make_password(password))
            if updateRec:

                #Send email
                subject, from_email, to = 'Nithcoin Password Reset', fromMail, ckUser.email
                text_content = 'You Requested for Password Reset.'
                html_content = '<h4>NITHCOIN</h4><hr>To Reset your password, please click the link below. <br><br> <a href="https://nithcoin.com/reset/confirm/'+ckUser.code+'">https://nithcoin.com/reset/confirm/'+ckUser.code+'</a><br><br>You may ignore if you did not requested for password reset.<br><br> Best Regards'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                Msg = 'Bravo. You are just one step away. <br>Please, check your mail to confirm password reset.'
                getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages"> '+Msg+'</p></div>'
                messages.error(request, getMsg)
    return render(request, 'auth_user/reset.html', context)

def confirm_reset(request, unique):
    context = {"siteSet":siteSet}

    ckUser = ResetPassword.objects.filter(code = unique).first()
    ckUser_ = ResetPassword.objects.filter(code = unique).exists()
    if ckUser_ == False:
        return HttpResponse('Sorry, we can not continue with the process')
    else:
        updateRec = User.objects.filter(id = ckUser.user_id).update(password = ckUser.temp_password)
        if updateRec:

            #Send email
            subject, from_email, to = 'Nithcoin Password Reset', fromMail, ckUser.email
            text_content = 'You Requested for Password Reset.'
            html_content = '<h4>NITHCOIN</h4><hr>You have successfully reset your password. <br><br> If this is not from you, you can quickly reset your password and report to us as soon as possible.<br><br> Best Regards'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            ResetPassword.objects.filter(code = unique).update(code = secrets.token_hex(16))

            return redirect('/login')

    return render(request, 'auth_user/reset.html', context)

def logUserOut(request):
	logout(request)
	return redirect('login')
