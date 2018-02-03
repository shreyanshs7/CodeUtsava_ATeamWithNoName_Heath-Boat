# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hearing(models.Model):
	id = models.AutoField(primary_key=True)
	pta = models.IntegerField()
	percentage = models.DecimalField(max_digits=5,decimal_places=2)