from django.shortcuts import render
from  .models import*
# Create your views here.
def service(request):
	service = ModelService.objects.all()
	return render(request,'services/services.html',{'service':service})