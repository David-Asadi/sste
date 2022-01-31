from django.shortcuts import render
from django.http import HttpResponse
from .models import PlastGal
# Create your views here.

def plasticPage(request):
    gallery = PlastGal.objects.all()
    return render(request, "plastic_gallery/plastic.html", {'gallery': gallery})