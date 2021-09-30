from django.contrib import admin
from .models import Vard1

class Vard1Admin(admin.ModelAdmin):
    list_display = ['first_name','email','profession']

admin.site.register(Vard1,Vard1Admin)