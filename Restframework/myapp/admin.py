from django.contrib import admin
from .models import userinfo

# Register your models here.

class userdata(admin.ModelAdmin):
    list_display=['name','city','email','mobile']

admin.site.register(userinfo,userdata)
