from django.conf.urls import url
from .views import *
from django.views.generic.base import TemplateView


app_name = 'login'

url_patterns = [
    #url('',login_view,name='index'),
    url('weather/',TemplateView.as_view(template_name='weather.html')),
]