from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Customers,PolicyDetails
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q, F, Count, Value, Sum
from django.db.models.functions import TruncMonth , ExtractMonth
import datetime
import json
import requests
import re

@csrf_exempt
def viewData(request):
    try:
        values_customer = PolicyDetails.objects.all().values()        
        
        return JsonResponse({"values_customer": list(values_customer)},status=200)
    except Exception as e:
        return JsonResponse({'message': 'Server Exception.'+str(e)}, status=500)

@csrf_exempt
def chartData(request):
    try:
        
        list_of_regions = ['North','South','East','West']
        data = PolicyDetails.objects.filter(customer__customer_region__in = list_of_regions).\
        annotate(mon=TruncMonth('date_of_purchase'),custRegion = F('customer__customer_region'),\
         month=ExtractMonth('date_of_purchase')).\
        values('month','custRegion').annotate(count=Count('policy_id')).order_by('month')
        out=[
                {"month":'Jan'},
                {"month":'Feb'},
                {"month":'Mar'},
                {"month":'Apr'},
                {"month":'May'},
                {"month":'Jun'},
                {"month":'Jul'},
                {"month":'Aug'},
                {"month":'Sep'},
                {"month":'Oct'},
                {"month":'Nov'},
                {"month":'Dec'},
        ]  
        for item in list(data):            
            r=item["custRegion"]
            out[item["month"]-1][r]=item["count"]
    
        return JsonResponse({"values_customer": out},status=200)
    except Exception as e:
        print(e)
        return JsonResponse({'message': 'Server Exception.'+str(e)}, status=500)

@csrf_exempt
def updateData(request):
    try:
        
        jsonReq = json.loads(request.body)['formvalues']

        PolicyDetails.objects.filter(policy_id = jsonReq['policy_id']).update(\
            date_of_purchase = jsonReq['date_of_purchase'],customer_id = jsonReq['customer_id'],\
            vehicle_segment = jsonReq['vehicle_segment'],premium = jsonReq['premium'])
        
        values_customer = PolicyDetails.objects.all().values()        
        
        return JsonResponse({"message":"Success","values_customer": list(values_customer)},status=200)

    except Exception as e:
        return JsonResponse({'message': 'Server Exception.'+str(e)}, status=500)
    

