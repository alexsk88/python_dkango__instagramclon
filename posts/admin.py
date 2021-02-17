""" Post Admin Class"""
from django.contrib import admin
# Models
from posts.models import Post 
# Register your models here.
admin.site.register(Post)
