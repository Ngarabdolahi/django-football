from django.contrib import admin
from django.urls import path ,include
from app01 import views

urlpatterns = [
    path('search/',views.search),
    path('majores/store/',views.majores_store),
    path('majores/get/all/',views.majores_get_all),
    path('teachers/search2/',views.teachers_search2),
    
]
