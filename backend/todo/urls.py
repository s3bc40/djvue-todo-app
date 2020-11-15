"""Todo Application urls"""
from django.urls import path
from todo import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('tasks/', views.TagList.as_view()),
    path('tasks/<int:pk>', views.TaskDetail.as_view()),
    path('tags/', views.TagList.as_view()),
    path('tags/<int:pk>', views.TagDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
