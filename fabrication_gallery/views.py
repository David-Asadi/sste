from django.shortcuts import render
from django.http import HttpResponse
from .models import FabGal
# Create your views here.

def fabPage(request):
    gallery = FabGal.objects.all()
    return render(request, "fabrication_gallery/fabrication.html", {'gallery': gallery})