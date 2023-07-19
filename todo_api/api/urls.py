from django.urls import path
from api import views

urlpatterns = [
    path('tasks/', views.Tasks.as_view()),
]
