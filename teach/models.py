from django.db import models

# Create your models here.

class Session(models.Model):
	session_name = models.CharField(max_length=500) 
	session_content = models.TextField()
	slug = models.SlugField(unique=True)
	audience = models.CharField(max_length=500) 
	session_date = models.DateTimeField() 
	booked = models.BooleanField(default = False) 
	booked_no = models.IntegerField(default=1)

	def get_absolute_url(self):
		return f"{self.slug}" 

	def get_booked_url(self):
		return f"{self.slug}/booked"
