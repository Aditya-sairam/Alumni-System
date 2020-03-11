from django.db import models

# Create your models here.

class Project(models.Model):
	Title = models.CharField(max_length=200)
	Abstract = models.TextField()
	Unique_name = models.SlugField(unique=True)
	Implementation = models.TextField() 
	Technology_Stack = models.TextField() 
	Working_ScrrenShots = models.ImageField(upload_to='media/image/',blank=True,null=True) 

	def get_absolute_url(self):
		return f"/project/{self.slug}" 