from django.db import models
class Task(models.Model):
    STATUS_CHOICES =[
        ('To Do','To Do'),
        ('In Progress','In Progress'),
        ('Done','Done'),
    ]
    task = models.TextField(max_length=200)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='To Do')
    
    def __str__(self):
        return self.task