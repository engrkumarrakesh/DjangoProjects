from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile, name='templates_03'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]

# handler404 = 'function_based_view_01.views.notfound' # This is the function that will be called when a 404 error is raised
