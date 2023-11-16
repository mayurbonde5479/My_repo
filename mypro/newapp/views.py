from django.shortcuts import redirect, render 
from .models import Member

def index(request):
    mem = Member.objects.all()
    return render(request,'index.html', {'mem':mem})

def add(request):
    return render(request, 'add.html')

def addrec(request):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['course']
    a = request.POST['city']

    mem = Member(firstname = x, lastname = y, course = z, city = a)
    mem.save()
    return redirect("/")

def delete(request, id):
    mem = Member.objects.get(id = id)
    mem.delete()
    return redirect("/")

def update(request, id):
    mem = Member.objects.get(id = id)
    return render(request, 'update.html',{'mem': mem})

def uprec(request,id):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['course']
    a = request.POST['city']

    mem = Member.objects.get(id = id)
    mem.firstname = x
    mem.lastname = y
    mem.course = z
    mem.city = a
    mem.save()
    return redirect("/")