from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update/<str:task_id>/', views.updatingTask, name='update'),
    path('delete/<str:task_id>/', views.deleteTask, name='delete'),
]
