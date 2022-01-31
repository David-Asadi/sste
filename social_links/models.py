from django.db import models

# Create your models here.
class SocialCat(models.Model):
	class Meta:
		verbose_name = 'Available social media links- view only'
		verbose_name_plural =  'Available social media links - view only'
	name = models.CharField(max_length=200, null=False, blank=False)
	def __str__(self):
		return (self.name)


class SocialMedia(models.Model):
	class Meta:
		verbose_name = 'Add your social media links here'
		verbose_name_plural =  'Add your social media links here'
	media_type = models.ForeignKey(SocialCat, null=True, on_delete=models.CASCADE)
	link = models.CharField(max_length=2048, null=False, blank=False)
	

	def __str__(self):
		return str(self.media_type)
	
	


