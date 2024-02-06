from django.contrib import admin
from django.urls import path,include
from .api import TaskListApi,RetrieveUpdateDestroyTaskApi,CreateTaskApi
urlpatterns = [
    path('',TaskListApi.as_view()),
    path('editTask/<int:pk>',RetrieveUpdateDestroyTaskApi.as_view()),
    path('create/',CreateTaskApi.as_view()),
    
]