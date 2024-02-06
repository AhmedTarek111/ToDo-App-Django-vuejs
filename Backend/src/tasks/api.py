from rest_framework.generics import *
from .models import Task
from .serializer import TaskSerailzer

class TaskListApi(ListAPIView):
    queryset = Task.objects.all()
    serializer_class =  TaskSerailzer
    
class DeleteTaskApi(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class =  TaskSerailzer

class UpdateTaskApi(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class =  TaskSerailzer
    
class CreateTaskApi(CreateAPIView):
    serializer_class = TaskSerailzer
    queryset = Task.objects.all()