from django.urls import path
from . import views

urlpatterns = [
    path('', views.dwellings_list, name='mn-main'),
    path('<int:id>/', views.dwelling_details, name='mn-details')
]