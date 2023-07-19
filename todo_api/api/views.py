from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response

# Create your views here.


class TasksView(APIView):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskView(APIView):
    def get(self, request, id, *args, **kwargs):
        task = Task.objects.filter(id=id)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
