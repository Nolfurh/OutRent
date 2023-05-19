from django.urls import path
from . import views

urlpatterns = [
    path('', views.DwellsListView.as_view(), name='home'), #home = search page
    path('<int:id>/', views.dwelling_details, name='dw-details'),
]