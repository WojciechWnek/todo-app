from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'tasks', views.TaskVeiwSet, basename="task")
# router.register(r'users', views.UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),
    path("auth/register/", views.UserRegister.as_view(), name="register"),
    path("auth/login/", views.UserLogin.as_view(), name="login"),
    path("auth/logout/", views.UserLogout.as_view(), name="logout"),
    path("auth/user/", views.UserView.as_view(), name="user"),
    # path('tasks/', views.TasksView.as_view()),
    # path('tasks/<int:id>/', views.TaskView.as_view()),
]
