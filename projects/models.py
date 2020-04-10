from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.

class Project(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
	Title = models.CharField(max_length=200)
	Abstract = models.TextField()
	slug = models.SlugField(unique=True)
	Implementation = models.TextField()
	Technology_Stack = models.TextField()
	Working_ScreenShots = models.ImageField(upload_to='Working_ScreenShots',blank=True,null=True)
	Likes = models.IntegerField(default=0)
	Person_Likes = models.IntegerField(default=0)
	#
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='post_likes')
	numb = models.IntegerField(default=0)
	numb_rem = models.IntegerField(default=100)
	state = models.BooleanField(default=False)



	def get_absolute_url(self):
		return f"/project/{self.slug}"

	def get_notabsolute_url(self):
		return f"/prolist/"

	def get_like_url(self):
		return reverse("likes" ,kwargs={"slug":self.slug})

	def get_apilike_url(self):
		return reverse("apilikes" ,kwargs={"slug":self.slug})
