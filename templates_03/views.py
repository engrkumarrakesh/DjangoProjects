from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactForm


# Create your views here.
def templates_03(request):
    gender="male"
    name={'name':'Kumar Rakesh','age':32,'gender':gender}
    # return render(request, 'index.html',context=name)
    # return render(request, 'index.html',{'name':'Kumar Rakesh'})
    return render(request, 'index.html',name)

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thank you for your message!')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})