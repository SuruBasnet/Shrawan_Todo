from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo


# Create your views here.
def home(request):
    todo_objects = ToDo.objects.all()
    content = {'todos':todo_objects}
    return render(request,'index.html',context=content)

def create(request):
    return render(request,'create.html')