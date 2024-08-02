from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class AdminEmployee(admin.ModelAdmin):
  list_display=["name","age","father_name","highest_education","gender","id"]