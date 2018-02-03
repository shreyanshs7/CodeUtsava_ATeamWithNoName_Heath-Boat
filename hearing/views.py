# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def HearingCalculate(request):
	try :
		if request.method == "POST":
			print(request.body)

			body = json.loads(request.body.decode('utf-8'))
			
			left_pta = body['left_pta']
			right_pta = body['right_pta']
			name = body['name']
			age = body['age']
			gender = body['gender']

			if not left_pta or not right_pta or not name or not age or not gender:
				data = {
					"success":False,
					"message":"Enter all the fields"
				}

				return JsonResponse(data,safe=False)

			left_pta_obj = Hearing.objects.get(pta=left_pta)
			right_pta_obj = Hearing.objects.get(pta=right_pta)

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

def chart(request):
	try:
		doc_obj = DoctorUser.objects.all()
		age_list = []
		percentage_list = []

		for obj in doc_obj:
			age_list.append(obj.age)
			percentage_list.append(int(obj.percentage))

		return render(request,"chart.html", {"age" : age_list , "percentage": percentage_list})	
	
	except Exception as e:
		print(str(e))
		data = {
			"success":False,
			"message":"An error occured"
		}

		return JsonResponse(data,safe=False)		
	
# def MaleChart(request):
# 	try:
# 		male_obj = DoctorUser.objects.filter(gender="M")

# 		