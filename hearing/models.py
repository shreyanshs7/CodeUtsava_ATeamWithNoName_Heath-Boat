# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hearing(models.Model):
	id = models.AutoField(primary_key=True)
	pta = models.IntegerField()
	percentage = models.DecimalField(max_digits=5,decimal_places=2)


class DoctorUser(models.Model):
	GENDER_CHOICES = (
		('Male','M'),
		('Female','F'),
		)
	id = models.AutoField(primary_key=True)	
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
	percentage = models.DecimalField(max_digits=5,decimal_places=2)