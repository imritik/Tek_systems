from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import VisitorForm,FilterForm
from .models import Visitor,Visitor_perma
from django.db.models import Q 
from django.views.generic import TemplateView, ListView

# Create your views here.
def display(request):
    instance = Visitor.objects.all().last()
    form = VisitorForm(request.POST or None,instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            visit= form.save(commit=False)
            visit1 = Visitor_perma(name=form.cleaned_data['name'],pincode=form.cleaned_data['pincode'],date=form.cleaned_data['date'], uid=form.cleaned_data['uid'], address=form.cleaned_data['address'],purpose=form.cleaned_data['purpose'],whoto=form.cleaned_data['whoto'],email=form.cleaned_data['email'],phone=form.cleaned_data['phone'])
            visit1.save()
            visit.save()

    return render(request,'home.html',{'form':form})



def get_queryset(request):
    query = request.GET.get('q')
    instance = Visitor_perma.objects.filter(uid__icontains=query).first()
    form = FilterForm(request.POST or None ,instance =instance)
    if request.method =='POST':
        if form.is_valid():
            visit= form.save(commit=False)
            visit1 = Visitor_perma(name=form.cleaned_data['name'],pincode=form.cleaned_data['pincode'],date=form.cleaned_data['date'], uid=form.cleaned_data['uid'], address=form.cleaned_data['address'],purpose=form.cleaned_data['purpose'],whoto=form.cleaned_data['whoto'],email=form.cleaned_data['email'],phone=form.cleaned_data['phone'])
            visit1.save()
            visit.save()
        duplicates = Visitor_perma.objects.values('phone')
        # for x in duplicates:
            
        # print()
        print(duplicates)
    return render(request,'home.html',{'form':form})
def main(request):
    return render(request,'main.html')

		
class HomePageView(TemplateView):
    template_name = 'home1.html'


				



    
