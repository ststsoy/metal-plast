from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path('calcmat',views.calcmat,name='calcmat'),
    
]
