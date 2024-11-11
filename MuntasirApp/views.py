from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    object_user = users.objects.all()
    object_project = project.objects.all()
    object_wreport = WasteReport.objects.all()
    context1 = {'object_user': object_user,
                 'object_project': object_project,
                'object_wreport': object_wreport,


    }
    return render(request,template_name='MuntasirApp\Home.html',context=context1)





def Services(request):
    return render(request,template_name='MuntasirApp\Services.html')

def Services_details(request):
    return render(request,template_name='MuntasirApp\Services_details.html')
