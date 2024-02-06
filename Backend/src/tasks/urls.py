from django.contrib import admin
from django.urls import path,include
from .api import TaskListApi,DeleteTaskApi,UpdateTaskApi,CreateTaskApi
urlpatterns = [
    path('',TaskListApi.as_view()),
    path('delete/<int:pk>',DeleteTaskApi.as_view()),
    path('update/<int:pk>',UpdateTaskApi.as_view()),
    path('create/',CreateTaskApi.as_view()),
    
]