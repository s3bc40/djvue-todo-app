"""Serializers for the models of the todo application"""
from rest_framework import serializers
from .models import Task, Tag


class TaskSerializer(serializers.ModelSerializer):
    """Allow to serialize our Task model for the API"""

    class Meta:
        model = Task
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """Allow to serialize our Tag model for the API"""
    class Meta:
        model = Tag
        fields = '__all__'
    