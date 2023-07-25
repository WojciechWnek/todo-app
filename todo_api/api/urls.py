from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'tasks', views.TaskVeiwSet, basename="task")

urlpatterns = [
    path('', include(router.urls)),
    # path('tasks/', views.TasksView.as_view()),
    # path('tasks/<int:id>/', views.TaskView.as_view()),
]
