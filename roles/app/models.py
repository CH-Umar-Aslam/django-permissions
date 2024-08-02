from django.db import models

# Create your models here.

class Employee(models.Model):
  Gender_Choices=[
    ("Male","Male"),
    ("Female","Female")
  ]
  Education_Choices=[
    ("SSC","SSC"),
    ("HSSC","HSSC"),
    ("BS","BS"),
    ("MS","MS"),
    ("PHD","PHD"),
  ] 
  name=models.CharField(max_length=50)
  gender=models.CharField(max_length=50,choices=Gender_Choices)
  highest_education=models.CharField (max_length=50,choices=Education_Choices)
  age=models.IntegerField()
  father_name=models.CharField (max_length=50)

