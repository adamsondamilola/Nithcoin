from django.forms import ModelForm
from django import forms

################
from wallet.models import proofs
from vendor.models import Vendors
from users.models import Users

class uploadPOPForm(ModelForm):
    class Meta:
        model= proofs
        fields= ["pop"]
        #fields= '__all__'
        exclude = ['user_id', 'transaction_id', 'status', 'date_added']

class uploadProfile(ModelForm):
    class Meta:
        model= Vendors
        fields= ["profile"]
        exclude = ['user_id', 'email', 'firstname', 'lastname', 'country', 'city',
        'mobile', 'whatsapp', 'cover', 'full_face', 'id_card',
        'proof_of_residence', 'status', 'minimum', 'selling_at', 'date_added']

class uploadId(ModelForm):
    class Meta:
        model= Vendors
        fields= ["id_card"]
        exclude = ['user_id', 'email', 'firstname', 'lastname', 'country', 'city',
        'mobile', 'whatsapp', 'profile', 'cover', 'full_face',
        'proof_of_residence', 'status', 'minimum', 'selling_at', 'date_added']


class uploadProfile_User(ModelForm):
    class Meta:
        model= Users
        fields= ["profile"]

class uploadId_User(ModelForm):
    class Meta:
        model= Users
        fields= ["id_card"]
