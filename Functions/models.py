from __future__ import unicode_literals
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.db.models.signals import post_save

from django.db.models.signals import *
import os
from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField( blank=True,default="static\abc1.jpg",null=True)#default = os.path.join(settings.STATIC_ROOT,'static','abc1.jpg'),
    count = models.IntegerField(default=0)
    rate=  models.IntegerField(default=0)
                            #)#upload_to='media/')
    #rate=models.IntegerField()
#(max_length=100) #upload_to='media/')


    def create_user_profile(sender, instance, created, **kwargs):
       if created:
        b=instance._profile_photo
        #c=instance._rate
        a=Profile.objects.create(user=instance,profile_photo=b)#,rate=c)

    post_save.connect(create_user_profile ,sender=User)


# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=200)
    #password = models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    college= models.CharField(max_length=200)

    def __str__(self):
        return self.username

   
class contactus(models.Model):
    email = models.EmailField(max_length=200)
    #password = models.CharField(max_length=200)
    name= models.CharField(max_length=300)
    message= models.CharField(max_length=9000)

    def __str__(self):
        return self.email

class students(models.Model):
    name=models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    course=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    experience=models.TextField(max_length=11000)
    
    def __str__(self):
        return self.name

class compsem1(models.Model):
    semester=models.CharField(max_length=20)
    code=models.CharField(max_length=20)
    branch=models.CharField(max_length=20)
    def __str__(self):
        return self.semester

class File(models.Model):
    name=models.CharField(max_length=200)
    sem=models.CharField(max_length=200)
    branch=models.CharField(max_length=200)
    main_file=models.FileField()
    code=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class contribute(models.Model):
     name_of_student=models.CharField(max_length=30)
     upload_file=models.FileField(upload_to='documents/')
     name_of_file=models.CharField(max_length=50)
     subject=models.CharField(max_length=100)
     subject_code =models.CharField(max_length=10)
    

