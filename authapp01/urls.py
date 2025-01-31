from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('userdashboard/', views.userdashboard, name='userdashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('changepass_without_old/', views.change_password_without_old_password, name='changepass_without_old'),
    path('userdetails/<int:id>/', views.userdetails, name='userdetails'),
]
# handler404 = 'function_based_view_01.views.notfound' # This is the function that will be called when a 404 error is raised
