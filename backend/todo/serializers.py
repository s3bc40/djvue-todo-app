"""Serializers for the models of the todo application"""
from rest_framework import serializers
from .models import Task, Tag


class TaskSerializer(serializers.Serializer):
    """Allow to serialize our Task model for the API"""
    tags = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Tag.objects.all())
    class Meta:
        model = Task
        fields = [field.name for field in Task._meta.get_fields()].append('tags')


class TagSerializer(serializers.Serializer):
    """Allow to serialize our Tag model for the API"""
    class Meta:
        model = Tag
        fields = '__all__'
    