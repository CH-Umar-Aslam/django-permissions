from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from rest_framework import serializers
from .serializer import UserSerializer
from rest_framework.authentication import SessionAuthentication
from .custom_permission import CustomPermission
from rest_framework.permissions import DjangoModelPermissions
# Create your views here.
from django.views.generic import TemplateView
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response


@api_view(["GET","POST"])
@permission_classes([CustomPermission])
@authentication_classes([SessionAuthentication])
def EmployeeView(request):
  # allowed_roles = ['HR','Manager','umar','Directr']
  # permission_classes = (DjangoModelPermissions,)
  # queryset=Employee.objects.all()
  # serializer_class=EmployeeSerializer
  # authentication_classes=[SessionAuthentication]
  # permission_classes=[CustomPermission]
  if request.method =="GET":
    stu=User.objects.all()
    serializer=UserSerializer(stu,many=True)
    return Response(serializer.data) #//
  if request.method =="POST":
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message":"user created","data":serializer.data,"status":status.HTTP_201_CREATED})

    return Response(serializer.errors,status=status.HTTP_402_BAD_REQUEST)


@api_view(["GET","PATCH","PUT","DELETE"])
@permission_classes([CustomPermission])
@authentication_classes([SessionAuthentication])
def EmployeeViewSet(request,pk):
  if request.method =="GET":
      id=pk
      stu=User.objects.get(id=id)
      serializer=UserSerializer(stu)
      return Response({"data":serializer.data})


  if request.method =="DELETE":
        stu=User.objects.get(id=id)
        stu.delete()
        return Response({'message': 'User deleted'},status=status.HTTP_204_NO_CONTENT)

  if request.method =="PUT":
    stu=User.objects.get(id=id)
    serializer=UserSerializer(stu,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message":"complete updated" ,"data":serializer.data})

    return Response(serializer.errors,status=status.HTTP_402_BAD_REQUEST)
  
  if request.method =="PATCH":
    id=pk
    stu=User.objects.get(id=id)
    serializer=UserSerializer(stu,data=request.data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({"message":"partial updated" ,"data":serializer.data})
    return Response(serializer.errors,status=status.HTTP_402_BAD_REQUEST)

