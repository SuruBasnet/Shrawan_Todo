from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo


# Create your views here.
def home(request):
    todo_objects = ToDo.objects.all()
    content = {'todos':todo_objects}
    return render(request,'index.html',context=content)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        ToDo.objects.create(name=name,description=description,status=status)
        return redirect('home')
    content = {'mode':'create'}
    return render(request,'create.html',context=content)

def edit(request,pk):
    content = {'mode':'edit'}
    todo_object = ToDo.objects.get(id=pk)
    return render(request,'create.html',context=content)