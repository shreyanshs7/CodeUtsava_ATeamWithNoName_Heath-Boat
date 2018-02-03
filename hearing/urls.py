from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
	url(r'^$', HearingCalculate),
	url(r'^chart/$', chart),
	url(r'^age/$', AgeChart),
    
    
]
