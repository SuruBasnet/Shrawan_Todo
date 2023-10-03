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
    todo_object = ToDo.objects.get(id=pk)
    content = {'mode':'edit','todo':todo_object}
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        todo_object.name = name
        todo_object.description = description
        todo_object.status = status
        todo_object.save()
        return redirect('home')
    return render(request,'create.html',context=content)

def delete(request,pk):
    todo_object = ToDo.objects.get(id=pk)
    todo_object.delete()
    return redirect('home')