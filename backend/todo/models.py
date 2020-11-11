"""Databse models for the TodoApp"""
from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    user = models.ForeignKey(
                            get_user_model(),
                            on_delete=models.CASCADE,
                            null=False
                            )
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_created=True, auto_now_add=True)
    date_updated = models.DateTimeField(
                                        auto_created=True,
                                        auto_now=True,
                                        auto_now_add=True
                                        )
    date_completed = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True)
    priority = models.IntegerField(null=True)
    # Todo tags
    