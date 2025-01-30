from django.urls import path
from . import views


urlpatterns = [
    path('', views.auth, name='authentication'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),


]
# handler404 = 'function_based_view_01.views.notfound' # This is the function that will be called when a 404 error is raised
