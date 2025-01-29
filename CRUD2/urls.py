from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_employee, name='create'),
    path('delete/<int:id>/', views.delete_employee, name='delete'),
    path('update/<int:id>/', views.update_employee, name='update'),
]
# handler404 = 'function_based_view_01.views.notfound' # This is the function that will be called when a 404 error is raised
