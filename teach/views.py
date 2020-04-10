from django.shortcuts import render,redirect
from django.shortcuts import render,get_object_or_404,redirect
#from .forms import SessionForm
from .models import Session
from datetime import datetime
from django.contrib import messages


 # Create your views here.


def list_view(request):
	time = datetime.now()
	qs = Session.objects.filter(session_date__gte=time)

	#expiration(qs)
	template_name = "teach/class.html"

	context = {"qs":qs}
	return render(request,template_name,context)

def detail_view(request,slug):
	obj = get_object_or_404(Session,slug=slug)
	template_name = 'teach/classd.html'
	context = {"obj":obj}
	return render(request,template_name,context)


def booked_view(request,slug):
	obj = get_object_or_404(Session,slug=slug)
	template_name = "teach/classbook.html"
	if(request.method == "POST"):
		obj.booked = True
		obj.save()
		messages.success(request,"The Slot has been booked Sucessfully!")
		return redirect("/class")

	context = {"obj":obj}
	return render(request,template_name,context)

def front_view(request):
	template_name = "teach/front.html"
	return render(request,template_name)



'''def expiration(qs):
	now = datetime.now()

	if qs.session_date > now:
		qs.delete()'''
