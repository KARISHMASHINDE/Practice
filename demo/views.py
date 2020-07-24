from django.shortcuts import render
from .models import FoodCategory,FoodDetails
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.core.exceptions import ObjectDoesNotExist
import ast
import json
from rest_framework import status
from django.http import Http404


# Create your views here.
@api_view(['GET','POST'])
def ListFoodCategory(request,pk=id):        
    if request.method == 'GET':
        data = []
        try:
            obj = FoodCategory.objects.all()
            print(obj)
            for x in obj:
                div = {
                    "id":x.id,
                    "FoodCategory":x.category_name
                    }
                data.append({"field": div})
            json_data= json.dumps(data,indent=4, sort_keys=True, default=str)
            res= ast.literal_eval(json_data)
            status_code = status.HTTP_200_OK
            return Response(res, status = status_code)
        except ObjectDoesNotExist:
            data = {"error": " obj does not exist"}
            status_code = status.HTTP_400_BAD_REQUEST 
            
@api_view(['GET','POST'])
def ListFoodDetails(request):
    if request.method == 'GET': 
        ids=request.GET.get("category_name")
        print('ids>>>>',ids)
        data=[]
        user = FoodDetails.objects.filter(category_id=ids)
        for x in user:
            dist={
            'id':x.id,
            'food_name':x.food_name,
            'Price':x.price
            
            }
            data.append({"field": dist})
        print(data)
        json_data= json.dumps(data,indent=4, sort_keys=True, default=str)
        status_code = status.HTTP_200_OK
        res= ast.literal_eval(json_data)
        return Response(res, status = status_code)  
    
    
    
@api_view(['GET','POST'])
def DishDetails(request):             
    if request.method == 'GET':
        ids=request.GET.get("food_name")
        print('ids>>>>',ids)
        data=[]
        user = FoodDetails.objects.filter(food_name=ids)
        for x in user:
            dist={
            'id':x.id,
            'food_name':x.food_name,
            'Price':x.price
            
            }
            data.append({"field": dist})
        print(data)
        json_data= json.dumps(data,indent=4, sort_keys=True, default=str)
        res= ast.literal_eval(json_data)
        status_code = status.HTTP_200_OK
        return Response(res, status = status_code)