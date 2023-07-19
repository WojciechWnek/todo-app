from django.urls import path
from api import views

urlpatterns = [
    path('tasks/', views.TasksView.as_view()),
    path('tasks/<int:id>/', views.TaskView.as_view()),
]
