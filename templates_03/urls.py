from django.urls import path
from . import views


urlpatterns = [
    path('', views.templates_03, name='templates_03'),
]

# handler404 = 'function_based_view_01.views.notfound' # This is the function that will be called when a 404 error is raised
