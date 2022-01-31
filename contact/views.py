from email import message
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def contact(request):
    
    
    if request.method == 'POST':
        template = render_to_string('contact/email_template.html', {'name':request.POST['name'], 'email':request.POST['email'], 'subject':request.POST['subject'], 'message':request.POST['message']})

        send_mail(
            'Contact Form',
            template, 
            settings.EMAIL_HOST_USER, 
            ['davidasadi@yahoo.co.uk'], 
            fail_silently=False)

        return HttpResponseRedirect('/success/')
    else: 
        return render(request, 'contact/contact.html')
    
    

def success(request):
    return render(request, 'contact/success.html')