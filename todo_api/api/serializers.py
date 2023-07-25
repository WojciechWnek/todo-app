from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserSerializer(ModelSerializer):
    task = PrimaryKeyRelatedField(
        many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'task']
