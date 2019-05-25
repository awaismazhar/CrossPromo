from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.conf import settings # new
from .import views 

urlpatterns = [
    path('AllAdvertismentapi/',views.AdvertismentList.as_view()),
    path('AdvertismentAPI/<pk>/',views.AdvertismentSingleList.as_view()),
]



