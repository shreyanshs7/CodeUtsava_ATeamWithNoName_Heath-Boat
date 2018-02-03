from django.conf.urls import url
from django.contrib import admin
from .views import HearningCalculate

urlpatterns = [
    url(r'/', HearningCalculate),
]
