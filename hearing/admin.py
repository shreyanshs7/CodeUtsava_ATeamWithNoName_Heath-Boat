# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Hearing
from django.contrib import admin

# Register your models here.
class HearingAdmin(admin.ModelAdmin):
	list_display = ['id','pta','percentage']
admin.site.register(Hearing,HearingAdmin)	