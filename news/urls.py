# pages/urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsPageView.as_view(), name='news_list'),
]
