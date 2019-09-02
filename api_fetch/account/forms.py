from django import forms
from .models import Temp

class VisitorForm(forms.ModelForm):
	class Meta:
		fields = ['name','uid','address','purpose','pincode','whoto','email','phone'] 
		model = Temp



