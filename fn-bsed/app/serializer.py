from .models import User
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User 
    fields = ['name', 'gender', 'highest_education', 'father_name','age','id']