from django.forms import ModelForm
from django import forms

################
from .models import Messages

class UploadFile(ModelForm):
    class Meta:
        model= Messages
        fields= ["photo"]
        #fields= '__all__'
        #exclude = ['username', 'cover_pic']
