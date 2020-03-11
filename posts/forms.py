from .models import Post 
from django import forms 


class PostModelForm(forms.ModelForm):
	class Meta:
		model = Post

		fields = ['title','current_company','content','planning','date','slug']
