from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.models import User
from django.views import View
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from account.models import Temp,Visitor_perma
from account.serializer import TempSerializer
from django.http import StreamingHttpResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from .forms import VisitorForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
import datetime
import csv
from django.utils.encoding import smart_str
from django_export_csv import render_csv_response
from .resources import VisitorResource
from djqscsv import render_to_csv_response
from djqscsv import write_csv
from datetime import timedelta
from django.utils import timezone

# Receving json data from android app using below api:

@api_view(['GET', 'POST','DELETE'])
def user_list(request):
    if request.method == 'GET':
        snippets = Temp.objects.all()
        serializer = TempSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TempSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()            
            return Response(serializer.data, status=201)            
        return Response(serializer.errors, status=400)      


def display(request):
    instance = Temp.objects.all().last()
    form = VisitorForm(request.POST or None,instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            visit= form.save(commit=False)
            visit1=Visitor_perma(name=form.cleaned_data['name'],uid=form.cleaned_data['uid'],address=form.cleaned_data['address']
            ,pincode=form.cleaned_data['pincode'],purpose=form.cleaned_data['purpose'],whoto=form.cleaned_data['whoto'],email=form.cleaned_data['email'],phone=form.cleaned_data['phone'])
            visit1.save()
            visit.save()
    return render(request,'home.html',{'form':form})



# ------------------------------------------------------------------------------------------------
# Filtering search records:


class HomePageView(TemplateView):
    template_name = 'search.html'


class SearchResultsView(ListView):  
    model = Visitor_perma
    template_name = 'search_result.html'

    def get_queryset(self): 
        query  =self.request.GET.get('nam')
        query2 =self.request.GET.get('dat1')
        query3 = timezone.now().date() - timedelta(days=8)
        query4 = timezone.now().date() - timedelta(days=15)
        query5 =self.request.GET.get('dat2')
        qu =Visitor_perma.objects.filter(
            Q(name__startswith=query) & Q(date__gte=query2, date__lt=query5))
        return qu



        #query2 = datetime.datetime.combine(query2, datetime.time.min)
        #query6=datetime.timedelta(days=1)+query5 
        # count = Visitor_perma.objects.filter(uid__icontains = uid ).count()
        # print(count)

        # with open('account/templates/foo.csv', 'wb') as csv_file:
        #     write_csv(qu, csv_file)


# def some_view(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="foo.csv"'
#     writer = csv.writer(response)
#     writer.writerow(['id', 'name', 'phone', 'email'])
#     return response


# def export(self,request):
#     # person_resource = VisitorResource()
#     queryset = .objects.filter()
#     dataset = queryset.export()
#     # dataset = qu.export()
#     response = HttpResponse(dataset.csv, content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="foo.csv"'
#     print(dataset.csv)
#     return response


            
        #     qu = Visitor_perma.objects.filter(
        #      Q(name__startswith=query) & Q(date__range=[query2, query5]))
        #     return qu
        #     with open('foo.csv', 'wb') as csv_file:
        #         write_csv(qu, csv_file)
            # dataset = person_resource.export(qu)
            # response = HttpResponse(dataset.csv, content_type='text/csv')
            # response['Content-Disposition'] = 'attachment; filename="persons.csv"'
            # print(dataset.csv) 
            
 

def csv_view(request):
    qu = Visitor_perma.objects.all()
    return render_to_csv_response(qu)



    # with open('foo.csv', 'wb') as csv_file:
    #     write_csv(qu, csv_file)

         

    # (objects.all()[:7])------------last seven records
    # if date is to be entered in range then use date__range
    #Q(date__range=[query2, query3]) 

#--------------------------------------------------------------------------------------

# Converting html based admin reports to pdf


# person_resource = VisitorResource()

# dataset.yaml

# this prints all the data into csv file

