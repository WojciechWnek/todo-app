from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
