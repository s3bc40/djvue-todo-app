"""Databse models for the TodoApp"""
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


class Tag(models.Model):
    """Tag allowing to define a Task by keywords"""
    name = models.CharField(max_length=20, blank=False)
    visibility = models.BooleanField()


class Task(models.Model):
    """Object oriented definition of a Task in a Todo Application"""
    # user = models.ForeignKey(
    #                         get_user_model(),
    #                         on_delete=models.CASCADE,
    #                         null=False
    #                         )
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_created=True, auto_now_add=True)
    date_updated = models.DateTimeField(
                                        auto_created=True,
                                        auto_now=True
                                        )
    date_completed = models.DateTimeField(null=True)
    completed = models.BooleanField()
    due_date = models.DateTimeField(null=True)
    priority = models.IntegerField(null=True) # Make it to ChoiceField
    tags = models.ManyToManyField(Tag)

    def is_completed(self):
        """Check if Task is completed to register data"""
        if self.completed:
            self.date_completed = datetime.now()
            return True
        return False
    