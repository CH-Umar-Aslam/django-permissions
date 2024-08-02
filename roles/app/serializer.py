from .models import Employee
from rest_framework import serializers
class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model=Employee 
    fields = ['name', 'gender', 'highest_education', 'father_name','age','id']