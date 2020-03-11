from django.shortcuts import render 
from .forms import PostModelForm 
from .models import Post
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here. 


def list_view(request):
	obj = Post.objects.all() 
	template_name = 'posts/list.html' 

	context = {"obj":obj} 

	return render(request,template_name,context)

def create_view(request):
	form = PostModelForm(request.POST or None) 
	if form.is_valid():
		form.save() 
		print(form)
		form = PostModelForm() 

	context = {"form":form} 
	template_name = "posts/create.html" 

	return render(request,template_name,context) 


def detail_view(request,slug):
	obj = get_object_or_404(Post,slug=slug)
	template_name = 'posts/detail.html' 
	context = {"obj":obj}

	return render(request,template_name,context)

