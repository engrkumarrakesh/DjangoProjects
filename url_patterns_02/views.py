from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def url_patterns(request):
    #Syntax
    #return render(request, template_name,context=dict_name, content_type=MIME_TYPE, status=status_code, using=None) # request is Object
    return HttpResponse("Hello URL Patterns 02")