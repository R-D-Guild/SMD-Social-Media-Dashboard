from django.urls import path
from . import views

urlpatterns=[
    path("Home/",views.Home,name="home"),
    path("Posting/",views.Posting,name="Posting"),]