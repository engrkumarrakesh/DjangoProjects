from django.shortcuts import render
from django.http import HttpResponse
from CRUD.models import Employee
from django.shortcuts import redirect
# Create your views here.
def index(request):
    emp=Employee.objects.all()
    return render(request, 'index.html',{'emp':emp})

def create(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        emp=Employee(name=name,email=email,address=address,phone=phone)
        emp.save()
    return redirect('index')

def edit(request, id):
    emp=Employee.objects.get(id=id)
    return redirect(request, 'index.html', {'emp':emp})

def update(request, id):
    # emp=Employee.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        emp= Employee(id=id,name=name,email=email,address=address,phone=phone)
        # emp.name=name
        # emp.email=email
        # emp.address=address
        # emp.phone=phone
        emp.save()
    return redirect('index')

def delete(request, id):
    emp=Employee.objects.filter(id=id)
    emp.delete()
    return redirect('index')