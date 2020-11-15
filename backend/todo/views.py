"""Todo application views"""
from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import render

# Task view
class TaskList(APIView):
    """List all tasks, or create one"""
    def get(self, request, format=None):
        """GET Request"""
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """POST Request"""
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    """Get detail about one specific Task

    Keyword arguments:
    pk -- primary key of the Task to identify it
    """
    def get_object(self, pk):
        """Get the Task with the corresponding primary key"""
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk,format=None):
        """GET Request"""
        task = self.get_object(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
   
    def put(self, request, pk, format=None):
        """PUT request to update Task"""
        task = self.get_object(pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Tag views
class TagList(generics.ListCreateAPIView):
    """Generic class API to show a list or create a Tag"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    """Generic class API to retrieve, update or destroy a Tag"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer