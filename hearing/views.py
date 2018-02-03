# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.
def HearningCalculate(request):
	try :
		if request.method == "POST":
			print(request.body)

			body = json.loads(request.body.decode('utf-8'))

			id = body['id']
			left_pta = body['left_pta']
			right_pta = body['right_pta']

			left_pta_obj = Hearning.objects.get(pta=left_pta)
			right_pta_obj = Hearning.objects.get(pta=right_pta)

			left_percentage = left_pta_obj.percentage
			right_percentage = right_pta_obj.percentage

			if left_pta>=right_pta:
				better_ear = left_percentage
				poorer_ear = right_percentage
			else:
				better_ear = right_percentage
				poorer_ear = left_percentage

			percentage_disability = (better_ear * 5 + poorer_ear)/6
			percentage_disability = round(percentage_disability,2)

			name = body['name']
			age = body['age']
			gender = body['gender']

			doctor_user_obj = DoctorUser.objects.create(
				name=name,
				age=age,
				gender=gender,
				percentage=percentage_disability
				)

			data = {
				"success" : True,
				"percentage_disability" : percentage_disability
			}

			return JsonResponse(data,safe=False)	
		
		else:

			data = {
			"success" : False,
			"message" : "Invalid request"
			}		

			return JsonResponse(data,safe=False)
	except Exception as e:
		print(str(e))
		data = {
		"success" : False,
		"message" : "An error occured"
		}

		return JsonResponse(data,safe=False)		