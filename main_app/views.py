from django.shortcuts import render
from .models import Dwelling, DwellingRentStatus, ReviewDwelling, ReviewRenter
from django.views.generic import ListView

class DwellsListView(ListView):
    model = Dwelling
    #queryset = Post.published.all()
    fields = ['title', 'card_description', 'owner']
    context_object_name = 'dwells'
    #paginate_by = 3
    template_name = 'main_app/home.html'

# def dwellings_list(request):
#     return render(request, 'main_app/home.html', {'dwells': Dwelling.objects.all()})


def dwelling_details(request, id):
    return render(request, 'main_app/details.html', {'dwells': Dwelling.objects.get(id=id)})
