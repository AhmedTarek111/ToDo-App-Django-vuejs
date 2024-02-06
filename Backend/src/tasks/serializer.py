from rest_framework import serializers
from .models import Task
class TaskSerailzer(serializers.ModelSerializer):
    class Meta:
        model =Task
        fields = ['id','task','status']