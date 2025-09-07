# news/views.py
from django.shortcuts import render
from django.views.generic import TemplateView


class NewsPageView(TemplateView):
    template_name = "news/news_page.html"
