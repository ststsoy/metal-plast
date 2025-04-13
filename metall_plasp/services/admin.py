from django.contrib import admin

# Register your models here.
from .models import*

admin.site.register(ModelService)
admin.site.register(Category)

