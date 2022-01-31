from social_links.models import SocialMedia, SocialCat

def soclinks(request):
	smedia = SocialMedia.objects.all()
	return{'smedia':smedia}
	