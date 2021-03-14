from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . models import employees
from . serializer import employeesSerializers
from django.http import JsonResponse

def view_data(request):#Example
    data ={
        "name":"sasas",
        "age":"12"
    }
    return JsonResponse(data)

class employeesList(APIView):
    def get(self,request):
        basicM = employees.objects.all()
        serializer = employeesSerializers(basicM, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = employeesSerializers(data=request.data)
        if serializer.is_valid():
            print("true Iam Inside")
            return Response(serializer.data)
        return Response(serializer.errors)
        
    

# Create your views here.
