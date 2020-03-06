from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def display_laptop(request):
    items = Laptop.objects.all()
    context = {'items':items,'header':"Laptop"}
    return render(request,'index.html',context)

def display_mobile(request):
    items = Mobile.objects.all()
    context = {'items':items,'header':"Mobile"}
    return render(request,'index.html',context)

def display_desktop(request):
    items = Desktop.objects.all()
    context = {'items':items,'header':"Desktop"}
    return render(request,'index.html',context)

def add_device(request,cls):
    if request.method == 'POST':
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        return render(request,'add_items.html',{'form':form})

def add_desktop(request):
    return add_device(request,DesktopForms)

def add_mobile(request):
    return add_device(request,MobileForms)

def add_laptop(request):
    return add_device(request,LaptopForms)

def edit_device(request,pk,cls,model):
    item = get_object_or_404(model,pk=pk)
    if request.method == 'POST':
        form = cls(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance = item)
        return render(request,'edit.html',{'form':form})

def edit_laptop(request,pk):
    return edit_device(request,pk,LaptopForms,Laptop)

def edit_desktop(request,pk):
    return edit_device(request,pk,DesktopForms,Desktop)

def edit_mobile(request,pk):
    return edit_device(request,pk,MobileForms,Mobile)

def delete_laptop(request,pk):
    Laptop.objects.filter(id=pk).delete()

    items = Laptop.objects.all()

    return render(request,'index.html',{'items':items})

def delete_mobile(request,pk):
    Mobile.objects.filter(id=pk).delete()

    items = Mobile.objects.all()

    return render(request,'index.html',{'items':items})

def delete_desktop(request,pk):
    Desktop.objects.filter(id=pk).delete()

    items = Desktop.objects.all()

    return render(request,'index.html',{'items':items})
