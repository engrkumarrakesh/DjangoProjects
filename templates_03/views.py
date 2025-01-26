from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactForm
from datetime import datetime


# Create your views here.
def templates_03(request):
    dt=datetime.now()
    gender="male"
    name={'name':'Kumar Rakesh','age':32,'gender':gender,'dt':dt}
    # return render(request, 'index.html',context=name)
    # return render(request, 'index.html',{'name':'Kumar Rakesh'})
    students={'name':['Rakesh Kumar','Sachin Tendulkar','Rahul Dravid']}
    return render(request, 'index.html',students)

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thank you for your message!')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})