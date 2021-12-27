from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'coffees'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.show, name='show'),
    path('add/', views.add, name='add'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]