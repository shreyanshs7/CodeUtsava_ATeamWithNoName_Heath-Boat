# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
	return render(request,"chart.html")


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
		male_obj = DoctorUser.objects.filter(gender="Male")
		female_obj = DoctorUser.objects.filter(gender="Female")
		male_list = []
		female_list = []

		for obj in male_obj:
			male_list.append(int(obj.percentage))

		for obj in female_obj:
			female_list.append(int(obj.percentage))	

		return render(request,"index.html", {"male" : male_list , "female": female_list})	
	
	except Exception as e:
		print(str(e))
		data = {
			"success":False,
			"message":"An error occured"
		}

		return JsonResponse(data,safe=False)		
	
def AgeChart(request):
	try:
		if request.method == "GET":
			age_20 = DoctorUser.objects.filter(age__lte=20).count()
			age_20_30 = DoctorUser.objects.filter(age__range=(20,30)).count()
			age_30_40 = DoctorUser.objects.filter(age__range=(30,40)).count()

			age_list = [age_20,age_20_30,age_30_40]

			data = {
				"success":True,
				"age_list" : age_list
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
			"success":False,
			"message":"An error occured"
		}

		return JsonResponse(data,safe=False)	