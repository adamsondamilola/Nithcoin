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
from django.contrib.auth.models import User, AbstractUser
from users.models import Users
from vendor.models import Vendors
from wallet.models import wallets
from .models import Messages

#forms
from uploads.forms import uploadProfile_User, uploadId_User
from .forms import UploadFile


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
def messenger(request, id):
    if id == request.user.id:
        return HttpResponse('You can not send message to yourself.')

    if Vendors.objects.filter(user_id = id).exists() == True:
        recv = Vendors.objects.filter(user_id = id).first()
        '''
        receiver_fname = recv.firstname
        receiver_lname = recv.lastname
        receiver_email = recv.email
        receiver_dp = recv.profile
        '''
    else:
        recv = Users.objects.filter(user_id = id).first()
        '''
        receiver_fname = recv.firstname
        receiver_lname = recv.lastname
        receiver_email = recv.email
        receiver_dp = recv.profile
        '''

    if Vendors.objects.filter(user_id = id).exists() == True:
        snd = Vendors.objects.filter(user_id = id).first()
        '''
        sender_fname = snd.firstname
        sender_lname = snd.lastname
        sender_email = snd.email
        sender_dp = snd.profile
        '''
    else:
        snd = Users.objects.filter(user_id = id).first()
        '''
        sender_fname = snd.firstname
        sender_lname = snd.lastname
        sender_email = snd.email
        sender_dp = snd.profile
        '''

    sentMsg = Messages.objects.filter(sender_id = request.user.id)
    ck1 = Messages.objects.filter(receiver_id = request.user.id, sender_id = id).first()
    if ck1:
        parentId = ck1.parent_id
    else:
        ck2 = Messages.objects.filter(sender_id = request.user.id, receiver_id = id).first()
        if ck2:
            parentId = ck2.parent_id
        else:
            parentId = 1 #default ID for null message
    if ck1 or ck2:
        viewMsg = Messages.objects.filter(parent_id = parentId)
    else:
        viewMsg = ''
    receivedMsg = Messages.objects.filter(receiver_id = request.user.id)
    getUser = Users.objects.filter(user_id = request.user.id).first()
    userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
    context = {'siteSet':siteSet,
    'userWallet':userWallet,
    'getUser':getUser,
    'snd':snd,
    'recv':recv,
    'parentId':parentId,
    'viewMsg':viewMsg,
    'id':id}
    checkRecs = Vendors.objects.filter(user_id = request.user.id).exists()
    status = 1

    if request.method == 'POST' and request.POST.get('posting'):
        photos = request.FILES.get('photo')
        pic_form = UploadFile(request.POST, request.FILES)
        if len(request.POST.get('message')) > 2000:
            msgOutput = 'Message is too long.'
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
            messages.error(request, getMsg)
        elif len(request.POST.get('message')) < 1 and pic_form.is_valid() == False:
            msgOutput = 'Nothing was sent.'
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
            messages.error(request, getMsg)
        elif request.FILES.get('photo') and len(request.POST.get('message')) < 1:
            lastMsg = Messages.objects.last()
            if lastMsg:
                lastId = lastMsg.id + 1
            else:
                lastId = 1
            if Messages.objects.filter(receiver_id = id, sender_id = request.user.id).exists():
                lastMsg = Messages.objects.filter(receiver_id = id, sender_id = request.user.id).last()
                lastId = lastMsg.parent_id
            elif Messages.objects.filter(receiver_id = request.user.id, sender_id = id).exists():
                lastMsg = Messages.objects.filter(receiver_id = request.user.id, sender_id = id).last()
                lastId = lastMsg.parent_id

            for file in request.FILES.getlist('photo'):
                instance = Messages(user_id = request.user.id,
            photo = file,
            sender_id = request.user.id,
            receiver_id = id,
            message = request.POST.get('message'),
            seen = 0,
            parent_id = lastId ,
            date_added = datetime.now()).save()
            #pic_form.save()

            msgOutput = 'Message sent!'
            getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
            #messages.error(request, getMsg)
            response = {'status':0, 'msg':getMsg}
            return JsonResponse(response)

        elif photos != None and len(request.POST.get('message')) > 0:
            lastMsg = Messages.objects.last()
            if lastMsg:
                lastId = lastMsg.id + 1
            else:
                lastId = 1
            if Messages.objects.filter(receiver_id = id, sender_id = request.user.id).exists():
                lastMsg = Messages.objects.filter(receiver_id = id, sender_id = request.user.id).last()
                lastId = lastMsg.parent_id
            elif Messages.objects.filter(receiver_id = request.user.id, sender_id = id).exists():
                lastMsg = Messages.objects.filter(receiver_id = request.user.id, sender_id = id).last()
                lastId = lastMsg.parent_id

            for file in request.FILES.getlist('photo'):
                instance = Messages(user_id = request.user.id,
                photo = file,
                sender_id = request.user.id,
                receiver_id = id,
                message = request.POST.get('message'),
                seen = 0,
                parent_id = lastId ,
                date_added = datetime.now()).save()
                #pic_form.save()

            msgOutput = 'Message sent!'
            getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
            #messages.error(request, getMsg)
            response = {'status':0, 'msg':getMsg}
            return JsonResponse(response)

        elif photos == None and len(request.POST.get('message')) > 0:
            lastMsg = Messages.objects.last()
            if lastMsg:
                lastId = lastMsg.id + 1
            else:
                lastId = 1
            if Messages.objects.filter(receiver_id = id, sender_id = request.user.id).exists():
                lastMsg = Messages.objects.filter(receiver_id = id, sender_id = request.user.id).last()
                lastId = lastMsg.parent_id
            elif Messages.objects.filter(receiver_id = request.user.id, sender_id = id).exists():
                lastMsg = Messages.objects.filter(receiver_id = request.user.id, sender_id = id).last()
                lastId = lastMsg.parent_id

            Messages(user_id = request.user.id, sender_id = request.user.id, receiver_id = id,
            message = request.POST.get('message'), seen = 0, parent_id = lastId , date_added = datetime.now()).save()
            #pic_form.save()

            msgOutput = 'Message sent!'
            getMsg = '<div class="alert alert-success alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
            #messages.error(request, getMsg)
            response = {'status':0, 'msg':getMsg}
            return JsonResponse(response)
        else:
            msgOutput = 'Error sending message. Please, try again.'
            getMsg = '<div class="alert alert-danger alert-success-style2 alert-st-bg1 alert-st-bg12"><button type="button" class="close sucess-op" data-dismiss="alert" aria-label="Close"><span class="icon-sc-cl" aria-hidden="true">&times;</span></button><p id="messages">' +msgOutput+ '</p></div>'
            #messages.error(request, getMsg)
            response = {'status':0, 'msg':getMsg}
            return JsonResponse(response)

    return render(request, 'messenger/messenger.html', context)

def inbox(request):
    sentMsg = Messages.objects.filter(sender_id = request.user.id)
    #receivedMsg = Messages.objects.filter(receiver_id = request.user.id).values('sender_id', 'receiver_id', 'message').distinct()
    receivedMsg = Messages.objects.filter(receiver_id = request.user.id).order_by('-id')
    genVendorProfile = Vendors.objects.filter()

    getUser = Users.objects.filter(user_id = request.user.id).first()
    getUserR = Users.objects.all()
    userWallet = wallets.objects.filter(user_id=request.user.id, type='NTC').first()
    context = {'siteSet':siteSet,
    'userWallet':userWallet,
    'getUser':getUser,
    'sentMsg':sentMsg,
    'receivedMsg':receivedMsg,
    'getUserR':getUserR,
    'genVendorProfile':genVendorProfile}

    return render(request, 'messenger/inbox.html', context)

def sent(request):
    context = {}

    return render(request, 'messenger/sent.html', context)

def requests(request):
    context = {}

    return render(request, 'messenger/requests.html', context)
