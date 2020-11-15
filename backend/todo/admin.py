""" DJango Admin interface to register models"""
from django.contrib import admin
from .models import Task, Tag


# Register models here
admin.site.register(Task)
admin.site.register(Tag)
