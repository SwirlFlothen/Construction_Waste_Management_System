from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,template_name='MuntasirApp\Home.html')

def Services(request):
    return render(request,template_name='MuntasirApp\Services.html')

def Services_details(request):
    return render(request,template_name='MuntasirApp\Services_details.html')