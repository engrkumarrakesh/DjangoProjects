from django.shortcuts import render,redirect
from CRUD2.models import Employee
from django.http import HttpResponse
from CRUD2.forms import EmployeeForm
# Create your views here.
def create_employee(request):
    if request.method == 'POST':
        fm = EmployeeForm(request.POST)
        if fm.is_valid():
            # form.save()
            # return HttpResponse('Thank you for your message!')
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            emp=Employee(name=nm,email=em,password=pw)
            emp.save()
            fm = EmployeeForm()
            # return HttpResponse('Thank you for your message!')
            
    else:
        fm = EmployeeForm() 
    emp=Employee.objects.all()
        
    return render(request, 'add_display.html', {'form' : fm , 'emp' : emp})

def update_employee(request, id):
    if request.method == 'POST':
        pi=Employee.objects.get(pk=id)
        fm=EmployeeForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('create')
    else:
        pi=Employee.objects.get(pk=id)
        fm=EmployeeForm(instance=pi)
    return render(request, 'update.html', {'id' : id, 'form' : fm})


def delete_employee(request, id):
    if request.method == 'POST':
        emp=Employee.objects.filter(pk=id)
        emp.delete()
        return redirect('create')

