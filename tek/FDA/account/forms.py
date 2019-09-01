from django import forms
from .models import Visitor,Visitor_perma

class VisitorForm(forms.ModelForm):
	class Meta:
		fields = ['name', 'pincode','date','uid','address','purpose','phone','email','whoto']
		model = Visitor
		

class FilterForm(forms.ModelForm):
	class Meta:
		model = Visitor_perma
		fields = ['name', 'pincode','date','uid','address','purpose','phone','email','whoto']
			