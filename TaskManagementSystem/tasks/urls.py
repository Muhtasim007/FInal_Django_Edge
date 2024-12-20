from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .api_views import TaskListCreateAPIView

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='api_tasks'),
]