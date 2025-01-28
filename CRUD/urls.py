from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/', views.edit, name='edit'),
    path('update/<str:id>/', views.update, name='update'),
    path('delete/<str:id>/', views.delete, name='delete'),
]
# handler404 = 'function_based_view_01.views.notfound' # This is the function that will be called when a 404 error is raised
