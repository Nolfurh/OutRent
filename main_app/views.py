from django.shortcuts import render
from .models import Dwelling, DwellingRentStatus, ReviewDwelling, ReviewRenter


def dwellings_list(request):
    return render(request, 'main_app/home.html', {'dwells': Dwelling.objects.all()})


def dwelling_details(request, id):
    return render(request, 'main_app/details.html', {'dwells': Dwelling.objects.get(id=id)})
