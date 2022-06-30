from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('update/', views.updateItem),
    path('delete/', views.deleteItem),
]
