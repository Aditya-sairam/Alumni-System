from django.db import models

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=500)  
	planning = models.TextField()
	current_company = models.CharField(max_length=200) 
	slug = models.SlugField(unique=True)
	content = models.TextField() 
	date = models.DateTimeField() 

	def get_absolute_url(self):
		return f"/blog/{self.slug}"



	