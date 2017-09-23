from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import users ,contactus
from captcha.fields import CaptchaField
from .models import Profile ,contribute

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        #contain info about this outer class
        model = User
        fields=['username','email','password']
class UploadForm(forms.ModelForm):
     class Meta:
        model = contribute
        fields = ('name_of_student','name_of_file','subject','subject_code','upload_file',)


class UserFormlog(forms.Form):
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()


class ContactForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        #contain info about this outer class
        model = contactus
        fields = ['name','email','message']


