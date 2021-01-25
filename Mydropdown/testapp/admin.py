from django.contrib import admin
from .models import *


# Register your models here.
#class registerAdmin(admin.ModelAdmin):

admin.site.register(Programming)
admin.site.register(Course)