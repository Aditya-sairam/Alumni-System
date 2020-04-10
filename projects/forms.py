from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ["Title","Abstract","slug","Implementation","Technology_Stack","Working_ScreenShots","numb"]
