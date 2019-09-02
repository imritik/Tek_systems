from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from account import views
from .views import SearchResultsView ,HomePageView

urlpatterns =[ 
    path('user/', views.user_list),
    path('',views.display),
    path('search/', HomePageView.as_view() , name='search'),
    path('search_result/', SearchResultsView.as_view() , name='search_result'),
    path('download/' , views.csv_view, name='download'),
]
