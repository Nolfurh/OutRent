from django.shortcuts import render

def home(request):
    return render(request, 'draft_app/index.html')