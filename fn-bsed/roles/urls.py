
from django.contrib import admin
from django.urls import path,include
# from rest_framework.routers import DefaultRouter
from app import views

urlpatterns =[   
    path('admin/', admin.site.urls),
    path('employee/',views.EmployeeView),
    path('employee/<int:pk>/',views.EmployeeViewSet)
]
