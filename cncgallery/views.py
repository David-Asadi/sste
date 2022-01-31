from django.shortcuts import render
from django.http import HttpResponse
from .models import CncGal
# Create your views here.


def cncPage(request):
    gallery = CncGal.objects.all()
    return render(request, "cncgallery/cnc.html", {'gallery': gallery})