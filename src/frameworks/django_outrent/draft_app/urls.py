from django.contrib import admin
from django.urls import path, include
from draft_app import views

urlpatterns = [
    path('', views.home),
]