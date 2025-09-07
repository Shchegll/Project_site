# pages/urls
from django.urls import path
from . import views

urlpatterns = [
    path("", views.AboutPageView.as_view(), name="home"),
    path("pages/", views.AboutPageView.as_view(), name="about"),
    path("news/", views.NewsPageView.as_view(), name="news"),

]
