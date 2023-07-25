from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets

from django.contrib.auth.models import User
# Create your views here.


# class TasksView(APIView):
#     def get(self, request, *args, **kwargs):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         data = request.data
#         serializer = TaskSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data)

# This is the same as code above
# class TasksView(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


# class TaskView(APIView):
#     def get(self, request, id, *args, **kwargs):
#         task = Task.objects.filter(id=id)
#         serializer =
# (task, many=True)
#         return Response(serializer.data)

#     def put(self, request, id, *args, **kwargs):
#         data = request.data
#         task = Task.objects.filter(id=id).first()
#         serializer = TaskSerializer(instance=task, data=data)

#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data)

#     def delete(self, request, id):
#         task = Task.objects.filter(id=id).first()
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def patch(self, request, id):
#         data = request.data
#         task = Task.objects.filter(id=id).first()
#         serializer = TaskSerializer(instance=task, data=data, partial=True)

#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data)

# This is the same as code above

# class TaskView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     # by default it should be "pk" and it also should be changed to "pk" in urls.py
#     lookup_field = "id"


class TaskVeiwSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
