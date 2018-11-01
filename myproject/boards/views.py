from django.http import HttpResponse
from django.urls import path

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')
