from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from rest_framework import serializers
from .serializer import EmployeeSerializer
# from rest_framework.authentication import SessionAuthentication
# from .custom_permission import CustomPermission
from rest_framework.permissions import DjangoModelPermissions
# Create your views here.
from django.views.generic import TemplateView


class EmployeeViewSet(viewsets.ModelViewSet):
  # allowed_roles = ['HR','Manager','umar','Directr']
  permission_classes = (DjangoModelPermissions,)
  queryset=Employee.objects.all()
  serializer_class=EmployeeSerializer
  # authentication_classes=[SessionAuthentication]
  # permission_classes=[CustomPermission]

  

