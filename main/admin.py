from django.contrib import admin
from .models import Main
from django.contrib.auth.models import Permission

# Register your models here.

admin.site.register(Main)
admin.site.register(Permission)
