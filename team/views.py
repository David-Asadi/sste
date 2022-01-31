from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def homePage(request):
    member = Member.objects.all()
    return render(request, "team/index.html", {'member': member})

