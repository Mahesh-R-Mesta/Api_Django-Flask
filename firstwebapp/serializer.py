#Serializer for creating json 
from rest_framework import serializers
from . models import employees
from django import forms

class employeesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = employees
#       fields = ('f_name','l_name') when specified data only has to convert in json
        fields = ('f_name','l_name','emp_id')
        
