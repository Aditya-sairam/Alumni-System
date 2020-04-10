from django.shortcuts import render
from .forms import ProjectForm
from .models import Project
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import RedirectView
from django.db.models import F

# Create your views here.

def create_view(request):
	form = ProjectForm(request.POST or None,request.FILES or None)

	if(form.is_valid()):
		form.save()
		form = ProjectForm()

	template_name = "projects/projectcreate.html"

	context = {"form":form}

	return render(request,template_name,context)

def list_view(request):
	obj = Project.objects.all()
	template_name = "projects/projectlist.html"
	context = {"obj":obj}

	return render(request,template_name,context)

def detail_view(request,slug):
	obj = get_object_or_404(Project,slug=slug)

	template_name = "projects/prodetail.html"

	if(request.method == "POST"):
		obj.numb_rem = obj.numb_rem - obj.numb
		obj.save()

	if(request.GET.get("mybtn")):
		obj = get_object_or_404(Project,slug=slug)
		
	context = {"obj":obj}

	return render(request,template_name,context)

class PostLikeToggle(RedirectView):
	def get_redirect_url(self,*args,**kwargs):
		slug = self.kwargs.get("slug")
		obj = get_object_or_404(Project,slug=slug)
		url_ = obj.get_notabsolute_url()
		user = self.request.user
		if user in obj.likes.all():
			obj.likes.remove(user)
		else:
			obj.likes.add(user)

		return url_

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class PostLikeAPIToggle(APIView):
	authentication_classes = [authentication.SessionAuthentication]
	permission_classes = [permissions.IsAuthenticated]
	def get(self, request,slug=None, format=None):
		#slug = self.kwargs.get("slug")
		obj = get_object_or_404(Project,slug=slug)
		url_ = obj.get_notabsolute_url()
		user = self.request.user
		updated = False
		liked = False
		if user.is_authenticated:
			if user in obj.likes.all():
				liked = False
				obj.likes.remove(user)
			else:
				liked = True
				obj.likes.add(user)
			updated = True
		data = {"updated":updated,"liked":liked}
		#usernames = [user.username for user in User.objects.all()]
		return Response(data)
