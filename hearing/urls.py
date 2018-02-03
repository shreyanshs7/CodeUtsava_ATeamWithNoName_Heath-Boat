from django.conf.urls import url
from django.contrib import admin
from .views import HearingCalculate,chart

urlpatterns = [
	url(r'^$', HearingCalculate),
	url(r'^chart/$', chart),
    
    
]
