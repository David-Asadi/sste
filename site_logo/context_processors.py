from site_logo.models import Change_Logo

def logoChange(request):
    logo = Change_Logo.objects.all()
    return{
        'logo': logo
    }