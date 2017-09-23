from django.db import models
from .models import users ,students ,contribute





from django.contrib import admin

# Register your models here.
admin.site.register(users)
admin.site.register(students)
admin.site.register(contribute)
