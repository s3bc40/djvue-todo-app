"""Databse models for the TodoApp"""
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model


class Tag(models.Model):
    """Tag allowing to define a Task by keywords"""
    name = models.CharField(max_length=20, blank=False)
    visibility = models.BooleanField()

    def __str__(self):
        """Show name instead of object on admin panel"""
        return self.name


class Task(models.Model):
    """Object oriented definition of a Task in a Todo Application"""
    # user = models.ForeignKey(
    #                         get_user_model(),
    #                         on_delete=models.CASCADE,
    #                         null=False
    #                         )


    class Priority(models.IntegerChoices):
        """Priority level choice into real numbers"""
        NOT_IMPORTANT = 1
        IMPORTANT = 2
        URGENT = 3


    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date_created = models.DateField(auto_created=True, auto_now_add=True)
    date_updated = models.DateField(
                                        auto_created=True,
                                        auto_now=True
                                        )
    date_completed = models.DateField(null=True, blank=True)
    completed = models.BooleanField()
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(null=True, choices=Priority.choices) # Make it to ChoiceField
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        """Show title instead of object on admin panel"""
        return self.title
    
    def is_completed(self):
        """Check if Task is completed to register data"""
        if self.completed:
            self.date_completed = datetime.now()
            return True
        return False
    