from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
	url(r'^$', chart),
	url(r'^calculate$', HearingCalculate),
	url(r'^chart/$', index),
	url(r'^age/$', AgeChart),
    
    
]