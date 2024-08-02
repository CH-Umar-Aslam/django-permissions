
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app import views
router=DefaultRouter()

router.register('employee',views.EmployeeViewSet,basename="employees")
urlpatterns = [   
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
