from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HTTPResponse

class HomePageView(TemplateView):
    template_name = 'pages/index.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'