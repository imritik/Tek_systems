from django.urls import path
from .views import display,get_queryset,HomePageView,main

urlpatterns = [

   path('display',display,name = 'display'),
   path('',main),
   path('search_results/', get_queryset, name='search_results') ,
   path('home', HomePageView.as_view(), name='home'),  
]