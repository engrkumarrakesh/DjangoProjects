from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('math/<int:num1>/<int:num2>/', views.math, name='math'),
    path('math/', views.math, name='math'),
]

# handler404 = 'function_based_view_01.views.notfound' # This is the function that will be called when a 404 error is raised
