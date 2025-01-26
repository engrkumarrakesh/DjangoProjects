
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('function_based_view_01.urls')),
    path('url_patterns_02/', include('url_patterns_02.urls')),
    # path('app_name/', include('url_patterns_02.urls')),
    path('templates/', include('templates_03.urls')),
]

# handler404 = 'function_based_view_01.views.notfound' # This is the function that will be called when a 404 error is raised


# if we manage single URLS 

# from app1 import views as app1_views
# from app2 import views as app2_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', app1_views.home, name='home'),
#     path('about/', app2_views.about, name='about'),