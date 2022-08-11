from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update/<str:list_id>/', views.updatingTask, name='update'),
    path('delete/<str:list_id>/', views.deleteTask, name='delete'),
]
