from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    object_user = users.objects.all()
    context1 = {'object_user': object_user}
    return render(request,template_name='MuntasirApp\Home.html',context=context1)

def Services(request):
    return render(request,template_name='MuntasirApp\Services.html')

def Services_details(request):
    return render(request,template_name='MuntasirApp\Services_details.html')
